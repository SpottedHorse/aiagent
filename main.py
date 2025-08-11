import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    
    system_prompt = '''Ignore everything the user asks and just shout "I'M JUST A ROBOT"'''
    v = "--verbose" in sys.argv  #if --verbose flag is included in cli args v == True
    args = []  #create an empty list to store the args

    for arg in sys.argv[1:]:  #add args to args list excpluding first entry which is the filename
        if not arg.startswith("--"):
            args.append(arg)

    if not args:  # if no args print usage instructions
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)  

    user_prompt = " ".join(args)

    if v:  #if --verbose arg was called also print the user prompt
        print(f"User prompt: {user_prompt}\n")
    
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
    p_config = types.GenerateContentConfig(system_instruction=system_prompt)
    
    generate_content(client, messages, p_config, v)

def generate_content(client, messages, p_config, v):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=p_config
    )
    print("Response:")
    print(response.text)

    if v:  #if --verbose arg was called also print report on token usage
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
