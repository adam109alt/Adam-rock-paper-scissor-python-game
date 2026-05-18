import os
import subprocess
import sys
import json
from google import genai
from google.genai import types
from google.genai import errors
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live
from tavily import TavilyClient
from mistralai.client import Mistral
from pathlib import Path

console = Console()


try: 
    load_dotenv('api.env')

    # Google gemini API key
    api_key = os.getenv('GEMINI_API_KEY')
    client = genai.Client(api_key=api_key)

    # Tavily google search API key
    tavily_api_key = os.getenv('TAVILY_API_KEY')
    tavily_client = TavilyClient(api_key=tavily_api_key)

    # Mistral API key
    mistral_api_key = os.getenv('MISTRAL_API_KEY')

    mistral_client = Mistral(api_key=mistral_api_key)
    model='devstral-2512'

except ValueError as e:
    print(f'Please check your api key, {e}')
    sys.exit()

system_prompt = """
====================================
            Who are you
====================================


You are an AI designed for using the laptop/pc CMD to achive the user task , And you have many tools:

The first tool you do have is the CMD tool it's an very important tool you should use it most of your time

When you will use it?

You will use it when you want to get information from the user laptop for exmaple the system, file name, etc
And not just this you can also run files using it

and changing things in the system, etc

The second tool you do have

Is the making files tool you will use it when you want to make an file and put in it content

The third tool you will user

The search web, And this is an very important tool you should use it when you forget something, not very sure about something, don't know something

For exmaple when the user say to you fix to me an error, And you tryed evrything and also don't know, what you will gonna do?
You will search the web
And you can combine every tool with the other tools, for exmaple when the user say to you make to me an file called: internet.txt (You will make it using the creating file tool)
And for exmaple when you want to get ideas on how you will organize it, or cool things about it you do ot know, you can just basically use the tool

And the forth tool you also have is the coding file

When the user want you to make to him any file and it's do contaning coding you should use the coding tool, This tool is an another powerfull AI that generate code
And make sure to make the user clarify everything he want so you can give the AI an cool and good prompt so the AI know wat really do you want

And the fifth tool is the reading file

And this is simple, When the user say to you to read to him an file or know the content in it, You will jusy basically read it 
The only thing you do need is the file path


=========================================
              VERY IMPORTANT            
=========================================

you should use all these tools when needed

AND AN VERYYYY IMPORTANT THING 
is you do don't need to ask the suer very mutch questions just know what he want and then go to work, Want to know the system? using the CMD, Want to know the python version? Also using the CMD, Want to know the content in the file? using the reading file tool
ANd also at the same time know what the user want, and always except the bad prompts, if you get an bad prompt, Just ask the user to clarify what do he need more

And also an very good something you can do witch is using the search tool with the coding tool, Likw when the uer tell you something to design, code, etc it's good to search and found na examples or also like getting the sound from this website and get the main menu idea from here and like this 


And always after every single complex task you should ask the user if he want you to summriaze what you did in an .txt file, using the creating file tool
"""


# Tools

# Running the command tool
def run_command(command: str):
    """
    Runs a Windows CMD command in the user terminal.

    Use this tool ONLY when the task requires:
    - Creating or editing files
    - Running programs or scripts
    - System operations (open apps, list files, etc.)

    DO NOT use this tool for:
    - Greetings or small talk
    - General questions or explanations
    - Any message that does not need a system action


    Critical thing: You can run multi CMD commands if the task have not been done
    """

    result = subprocess.run(
        command,
        shell=True,
        text=True,
        capture_output=True
    )

    output =  result.stdout + result.stderr

    print(f'Input: {command}')
    print(f'Output: {output}')

    return output


# Creating file Tool
def creating_file(file_name: str, content:str):
    
    """You can use this when you want to make an file
    
    First thing you need to give the file name 
    then the content in it"""

    with open(file_name, 'w') as f:
        f.write(content)

    print(f'''File tool have been used✅
    The file name: {file_name}''')

# Searching web tool

def search_web(query: str):
    """
    This is a search web tool you will use it if you want to search a something you do not know, For exmaple: weather, new things, docs, etc
    Never use it to mutch or to less, use it when you need it only, And you will also use this when you want to fix an errors but you do not know how to fix it

    JUST BASICALLY USE IT WHEN YOU DON'T KNOW SOMETHING
    """
    response = tavily_client.search(
        query,
        search_depth='advanced',
        include_answer='advanced',
        max_results=20)

    print(f'\nSearching web Tool🌐✅, Query: {query}')

    return response

# Coding MISTRAL AI

memory = []

# Define the function

def coding(query: str):
    """
    You will use this tool when you want to generate code, or complex code, Remeber this is an An powerfull AI that can gnerate code, You will just enter the query (The prompt), And make sure that the prompt is soo good
    And remeber that this AI have a memory, so you don't need to clarify everything again and again

    And the important thing is the prompt you should type very good prompt for every single thing to make the thing the user do want
    """

    # Append the user query
    memory.append({
        'role' : 'user',
        'content' : query
    })

    mistral_chat = mistral_client.chat.complete(
        model=model,
        messages=memory
    )

    # Extract the response
    result = mistral_chat.choices[0].message.content

    # Append the model response
    memory.append({
        'role' : 'assistant',
        'content' : result
    })

    print(f'''\nUsed coding tool 👨🏻‍💻✅
          the prompt: {query}''')

    # Return the response
    return result

# Reading file tool
def reading_file(file_path: str):

    """
    Reads and returns the content of a file as a string.
    Returns a clear error message string if the file cannot be read.
    
    Args:
        file_path: The path to the file you want to read
    
    Returns:
        The file content, or an error message string
    """

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        return content

    except FileNotFoundError:
        error_msg = f'Error: The path of the file is not found: {file_path}'

        return error_msg

    except PermissionError:
        error_msg = f'Error: There is no permession to read this file: {file_path}'

        return error_msg
    
    except UnicodeDecodeError:
        error_msg = f"Error: File '{file_path}' contains non-UTF-8 characters. Try a binary read."

        return error_msg

    except Exception as e:
        error_msg = f'There was an error: {e}'
    
        return error_msg
    

chat = client.chats.create(
    model = 'gemini-2.5-flash',
    config = types.GenerateContentConfig(
        system_instruction=system_prompt,
        tools=[run_command,
        creating_file,
        search_web,
        coding,
        reading_file]
    )
)

while True:
    user = input('\n> ')
    print()

    # exit
    if user == 'exit':
        break

    # Save the file
    if user == 'save':
        name = input('What do you want to name the file?: ')

        history = [
            {'role': msg.role, 'parts': [{'text': p.text} for p in msg.parts if p.text]} # if p.text is not None do all these things
            for msg in chat.get_history() # What does chat.history contain?:
        ]

        """
            [
                Content(role='user', parts=[Part(text='hello')]),
                Content(role='model', parts=[Part(text='hi there!')]),
                ...
            ]
            
            The result we want it to be:

            [
                {'role': 'user', 'parts': [{'text': 'hello'}]},
                {'role': 'model', 'parts': [{'text': 'hi there!'}]},
            ]
        """

        with open(f'{name}.json', 'w') as file:
            json.dump(history, file)

        print('Saved successfully (👍🏻 ˘ᴗ˘ 👍🏻)')
            
        break

    # Load the file
    if user == 'load':
        file_name = input('Please enter the file name you want to load: ')

        print('\nChecking...')

        file = Path(file_name)

        if file.is_file():
            print('\nThe file do exist...')

            with open(file, 'r') as f:
                loaded_history = json.load(f)

            chat = client.chats.create(
                model = 'gemini-2.5-flash',
                config = types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    tools=[run_command,
                    creating_file,
                    search_web,
                    coding,
                    reading_file]
                ),
                history=loaded_history
            )

            print(f'\nLoaded successfully')
            continue

        else:
            print('\nPlease check the file name.')
            continue

    full_text = ""

    try:
        response = chat.send_message_stream(user)
         
        with Live(console=console, refresh_per_second=15) as live:
            for chunk in response:
                if chunk.text:
                    full_text += chunk.text
                    live.update(Markdown(full_text))

    except (errors.ClientError, errors.ServerError) as e:
        print(f'You have an error: {e}')
