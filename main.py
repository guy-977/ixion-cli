import openai
import subprocess

openai.api_key = "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"

def generate():
    prompt = input("write your prompt")
    messages= [
    {"role": "system", "content": "You are a helpful assistant."},
     {"role": "user", "content": f"write a command to do the following: {prompt}, format the command between three backticks"},
     ]
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=50,
    temperature=0.9,
    frequency_penalty=0.5,
    presence_penalty=0.5,
    messages=messages)
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
command_string = command[1].replace('\n', '')
print(f'the command string is{command_string}')

r = subprocess.run(command, shell=True, capture_output=True)
print(r)