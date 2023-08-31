import openai
import subprocess
import os

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')

prompt = input("write your prompt")
messages= [
    {"role": "system", "content": "Act as a penetration tester"},
     {"role": "user", "content": f"write a command to do the following: {prompt}, format the command between three backticks"},
     ]

def generate():
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=50,
    temperature=0.9,
    frequency_penalty=0.5,
    presence_penalty=0.5,
    messages=messages)
    messages.append(response['choices'][0]['message'])
    return response['choices'][0]['message']['content']


def get_text_between_backticks(s):
  # split by ```
  s = s.split ("```")
  # join only those elements at odd indices with a space
  s = ' '.join (s [i] for i in range (1, len (s), 2))
  # return the result
  return s


result = generate()

print(f'the model response is {result}')
command = get_text_between_backticks(result)
print(f'the command is {command}')

r = subprocess.run(command, shell=True, capture_output=True)
print(r)