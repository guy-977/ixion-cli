import openai
import re
from dotenv import load_dotenv
# load_dotenv()
# openai.api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = "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"

messages = [
    {"role": "system", "content": "you are a command line assistant"},
]


def generate_command(msg_array, pmt):
    msg_array.append(
        {"role": "user", "content": f"you are a command line assistant, do the following {pmt}, format the commands between three backticks and starting with the tool name"}
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=70,
        temperature=0.6,
        frequency_penalty=0.5,
        presence_penalty=0.5,
        messages=msg_array)
    msg_array.append(response['choices'][0]['message'])
    response = response['choices'][0]['message']['content']
    command = get_text_between_backticks(response)
    return response, command


def get_text_between_backticks(text):
    return re.findall(r'```(.*?)\n?(.*?)\n?```', text, re.DOTALL)[0][1]
