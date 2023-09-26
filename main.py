import subprocess
from llm import *


def excute_command(cmd):
    if input('\ndo you want to excute the command?(Y/n) ').lower() == "y":
        print('\nrunning...')
        try:
            output = subprocess.run(
                cmd, shell=True, capture_output=True, timeout=60).stdout.decode('utf-8')
            print('\nproccess has been excuted')
            messages.append(
                {"role": 'user', "content": f"this is the process output: {output}"}
            )
            print(output)
        except subprocess.TimeoutExpired:
            print('process timed out after 60 seconds')
        print('...................................')


while True:
    prompt = input(
        'enter prompt: ')
    response, command = generate_command(messages, prompt)
    print(f'\n\nthe AI response is {response} \nthe command is {command}')
    excute_command(command)
