import subprocess
import argparse
from llm import generate, messages, get_text_between_backticks

parser = argparse.ArgumentParser()
parser.add_argument('--prompt', action='store', required=True, help='The user prompt')
args = parser.parse_args()
prompt = args.prompt



try:
  messages = messages
  result = generate(messages, prompt)
  print(f'\n\nthe model response is {result}')
  command = get_text_between_backticks(result)
  print(f'\n\nthe command is {command}')
  if (input("\nDo you want to excute the command? (Y/n): ") == 'Y'):
      r = subprocess.run(command, shell=True, capture_output=True)
      print(r.stdout.decode("utf-8"))
      while True:
        if(input("\n Do you want to go further? (Y/n): ") == "Y"):
          messages.append({'role': 'user', 'content': f'using this information \n{r.stdout}\nWhat should I do to go further?'})
          result = generate(messages, prompt)
          print(result)
          print(f'\nthe model response is {result}')
        else:
           exit('session terminated')

  print(f'\n\nmessages are:{messages}')
  exit('session terminated')
except Exception as e:
   print(e)