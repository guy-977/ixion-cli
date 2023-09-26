import subprocess
import argparse
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


parser = argparse.ArgumentParser(description="devcli bestest")
parser.add_argument("--prompt", "-p", help="the prompt for the ai (optional)")
parser.add_argument("--temprature", "-t",
                    help="temprature of the model", default=0.6, type=float)

args = parser.parse_args()
if args.prompt:
    response, command = generate_command(
        messages, args.prompt, args.temprature)
    print(f'\n\nthe AI response is {response} \nthe command is {command}')
    excute_command(command)
while True:
    prompt = input(
        'enter prompt: ')
    response, command = generate_command(messages, prompt, args.temprature)
    print(f'\n\nthe AI response is {response} \nthe command is {command}')
    excute_command(command)
