import openai
import re
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

messages = [
    {"role": "system", "content": "you are a command line assistant"},
]


def generate_command(msg_array, pmt, temperature=0.6):
    msg_array.append(
        {"role": "user", "content": f"you are a command line assistant, do the following {pmt}, format the commands between three backticks and starting with the tool name"}
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=70,
        temperature=temperature,
        frequency_penalty=0.5,
        presence_penalty=0.5,
        messages=msg_array)
    msg_array.append(response['choices'][0]['message'])
    response = response['choices'][0]['message']['content']
    command = get_text_between_backticks(response)
    return response, command


def get_text_between_backticks(text):
    return re.findall(r'```(.*?)\n?(.*?)\n?```', text, re.DOTALL)[0][1]
