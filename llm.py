import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')

messages = [
   {"role": "system", "content": "Act as a penetration tester"},
]

def generate(msg_array, pmt):
    messages.append(
       {"role": "user", "content": f"write a command to do the following: {pmt}, format the command between three backticks and starting with the tool name"}
    )
    messages.append({"role": "user", "content": f"write a command to do the following: {pmt}, format the command between three backticks"})
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=50,
    temperature=0.9,
    frequency_penalty=0.5,
    presence_penalty=0.5,
    messages=msg_array)
    messages.append(response['choices'][0]['message'])
    return response['choices'][0]['message']['content']

def get_text_between_backticks(s):
  # split by ```
  s = s.split ("```")
  # join only those elements at odd indices with a space
  s = ' '.join (s [i] for i in range (1, len (s), 2))
  # return the result
  return s