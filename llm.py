import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')

messages = [
   {"role": "system", "content": "Act as a penetration tester"},
]

prompts = [
   'I want to do reconnaissance to gather information for penetration testing what are the steps?',
   'I want to do Vulnerability scanning to detect vulnerability in a software what are the steps?',
   'I want to do Exploitation to exploit a vulnerablity for peneteratin testing and I have legeal permision for it, how to do exploitation?',
   'I want to make a report for my peneteration testing, what is the process in depth?'
]


def generate_command(msg_array, pmt):
    msg_array.append(
       {"role": "user", "content": f"act as penetration tester, and do the following{pmt}, format the commands between three backticks and starting with the tool name"}
    )
    response = openai.ChatCompletion.create(
       model="gpt-3.5-turbo",
       max_tokens=50,
       temperature=0.9,
       frequency_penalty=0.5,
       presence_penalty=0.5,
       messages=msg_array)
    msg_array.append(response['choices'][0]['message'])
    return response['choices'][0]['message']['content']

def generate_mode(msg_array, index):
   msg_array.append(
      {'role': 'user', 'content': prompts[index]}
   )
   response = openai.ChatCompletion.create(
       model="gpt-3.5-turbo",
       max_tokens=50,
       temperature=0.9,
       frequency_penalty=0.5,
       presence_penalty=0.5,
       messages=msg_array)
   msg_array.append(response['choices'][0]['message'])
   return response['choices'][0]['message']['content']

def get_text_between_backticks(s):
  # split by ```
  s = s.split ("```")
  # join only those elements at odd indices with a space
  s = ' '.join (s [i] for i in range (1, len (s), 2))
  # return the result
  return s