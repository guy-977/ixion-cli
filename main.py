import subprocess
import argparse
from llm import *

## arguments parser to get input for the user's arguments before excuting the program
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--prompt', action='store', help='The user prompt', type=str)
parser.add_argument('-r', '--recon', action='store', help="run the program in reconnaissance mode", type=bool)
parser.add_argument('-v', '--vuln', action='store', help="run the program in vulnerability scanning mode ", type=bool)
parser.add_argument('-e', '--exploit', action='store', help="run the program in exploitation mode", type=bool)
parser.add_argument('-t', '--report', action='store', help="run the program in reporting mode", type=bool)

args = parser.parse_args()
prompt = args.prompt

# list of main four stages in penetration testing
modes = [
   'reconnaissance => tap r', 'vulnerability scanning => tap v', 'exploitation => tap e', 'reporting => tap rp'
]

# function to excute commands extracted from GPT's response
def excute_command(cmd):
   if(input('\ndo you want to excute the command?(Y/n) ') == "Y"):
      print('\nrunning...')
      try:
         output = subprocess.run(cmd, shell=True, capture_output=True, timeout=40).stdout.decode('utf-8')
         print('\nproccess has been excuted')
         messages.append(
            {"role": 'user', "content": f"this is the process output: {output}"}
            )
         print(output)
      except TimeoutError:
         print('process timed out after 40 seconds')
      print('\n...................................')
      
# 1 First method

try:
   # Ask the user to choose one of the main pentesting stages to get a roadmap of how to get started
   for i in modes:
      print(i)

   mode=input("\nChoose one: ")

   if(mode =='r'):
      print(generate_mode(messages,0)) 
      result = generate_mode(messages,0)
      print(result)
   elif(mode =='v'):
      print(generate_mode(messages,1))
      result = generate_mode(messages,1)
      print(result)
   elif(mode =='e'):
      print(generate_mode(messages,2))
      result = generate_mode(messages,2)
      print(result)
   elif(mode =='r'):
      print(generate_mode(messages,3))
      result = generate_mode(messages,3)
      print(result)
   
   #if user have inserted a prompt in --prompt argument
   if(prompt):
      #ask him if he want to continue or chage it
      if(input('\nYou inserted a prompt, do you want to use it?(Y/n)') == 'Y'):
         pass
      #if he want to change the prompt
      else:
         prompt = input('\nwhat do you want to do? (mention the tool name and the porpuse): ')   
   #if not as him to write a prompt
   else:
      prompt = input('\nwhat do you want to do next? (mention the tool name and the porpuse): ')
   #generate a response to user's prompt and extract a command
   response, command = generate_command(messages, prompt)
   print(f'\n\nthe AI response is {response} \nthe command is {command}')
   #call the command excution funtion
   excute_command(command)
   #ask if user want to do another task
   if (input('\ndo you want to do another task?(Y/n)') == 'Y'):
         while True:
            print("\nto stop the program click CTRL+C")
            prompt = input('\nwhat do you want next? (mention the tool name and the porpuse): ')
            response, command = generate_command(messages, prompt)
            print(f'\n\n the AI response is {response} \nthe command is {command}')
            excute_command(command)
            if("\ndo you want to continue?(Y,n)" == 'n'):
               break
   #terminate the program        
   print(f'\n\nmessages are:{messages}')
   exit('session terminated')
except KeyboardInterrupt as e:
   print("\nthe user terminated the program")



#2 Second Method


# try:
#   result = generate_command(messages, prompt)

#   print(f'\n\nthe model response is {result}')

#   command = get_text_between_backticks(result)

#   #I add those to check reconnaissance exploitation .........


#   if args.recon is not None and args.recon:
#     print(generate_mode(messages,0)) 
#     result = generate_mode(messages,0)
#   elif args.vuln is not None and args.recon:
#     print(generate_mode(messages,1)) 
#     result = generate_mode(messages,1)
#   elif args.exploit is not None and args.exploit:
#     print(generate_mode(messages,2)) 
#     result = generate_mode(messages,2)
#   elif args.report is not None and args.report:
#     print(generate_mode(messages,3)) 
#     result = generate_mode(messages,3)

#   ##########
     
#   print(f'\n\nthe command is {command}')

#   if (input("\nDo you want to continue with this command? (Y/n): ") == 'Y'):
#       r = subprocess.run(command, shell=True, capture_output=True)
#       print(r.stdout.decode("utf-8"))
#       while True:
#         if(input("\n Do you want to go further? (Y/n): ") == "Y"):
#           messages.append({'role': 'user', 'content': f'using this information \n{r.stdout}\nWhat should I do to go further?'})

#           # i just change prompt to result to use again in the next step

#           result = generate_command(messages, result)
#           print(result)
#           print(f'\nthe model response is {result}')
#         else:
#            exit('session terminated')

#   print(f'\n\nmessages are:{messages}')
#   exit('session terminated')
# except KeyboardInterrupt as e:
#    print("\nthe user terminated the program")