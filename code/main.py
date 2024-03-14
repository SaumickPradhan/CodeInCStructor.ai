import openai
import requests
import json
import sys


def get_api_key_from_file(filename):
    with open(filename, 'r') as f:
        api_key = f.read().strip()
    return api_key

openai.api_key = get_api_key_from_file('openaikey.txt')

def interact_with_gpt(user_input, conversation_history):
    context = ""

    conversation_history.append({"role": "user", "content": user_input})
    conversation_history.append({"role": "assistant", "content": context})

    data = {
        "model": "gpt-3.5-turbo",
        "messages": conversation_history,
        "max_tokens": 1200,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    }

    print("Sending request to OpenAI API...")
    response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
    print("Received response from OpenAI API")
                    
    response_data = response.json()

    print("Conversation history:", conversation_history)
    print("Response data:", response_data)

    if response_data.get("choices") and response_data["choices"][0].get("message"):
        assistant_response = response_data["choices"][0]["message"]["content"].strip()
        conversation_history.append({"role": "assistant", "content": assistant_response})

        result = {"response": assistant_response}
        return result

with open('index_map.json', 'r') as f:
    index_map = json.load(f)

conversation_history = [{"role": "system", "content": "You are a GPT-3.5 coding assistant helping with coding questions. Do not give away the right answer to coding questions. DO NOT DO  THAT EVER. Just give feedback to whatever the student asks about coding. If the question is wrong, just give hints on how to get to the right answer. DO NOT SAY THE RIGHT ANSWER."}]