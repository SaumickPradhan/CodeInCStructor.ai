# import openai
# import requests
# import json
# import sys
# from flask import request
# import json



# with open('Questionbank.json', 'r') as f:
#     question_bank = json.load(f)

# def get_api_key_from_file(filename):
#     with open(filename, 'r') as f:
#         api_key = f.read().strip()
#     return api_key

# openai.api_key = get_api_key_from_file('openaikey.txt')

# def interact_with_gpt(user_input, conversation_history, assignment_name):
#     print(assignment_name,"dseds")
    
#     context = "The question (only for your context, do not give away answer) is: " + question_bank[assignment_name] if assignment_name in question_bank else  "" + " Check if user's response is related to this question. Do not respond if response is not related to this question. Do Not give away the answer." #Write a Python function that takes a list of integers as input and returns a new list containing only the unique elements of the original list, maintaining the original order. 

#     conversation_history.append({"role": "user", "content": user_input})
#     conversation_history.append({"role": "system", "content": context})

#     data = {
#         "model": "gpt-3.5-turbo",
#         "messages": conversation_history,
#         "max_tokens": 1200,
#     }

#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {openai.api_key}"
        
#     }

#     print("Sending request to OpenAI API...")
#     response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
#     print("Received response from OpenAI API")
                    
#     response_data = response.json()

#     print("Conversation history:", conversation_history)
#     print("Response data:", response_data)

#     if response_data.get("choices") and response_data["choices"][0].get("message"):
#         assistant_response = response_data["choices"][0]["message"]["content"].strip()
#         conversation_history.append({"role": "assistant", "content": assistant_response})

#         result = {"response": assistant_response}
#         return result


# conversation_history = [{"role": "system", "content": "You are a GPT-3.5 coding assistant helping with coding questions. Do not give away the right answer to coding questions. DO NOT DO  THAT EVER. Just give feedback to whatever the student asks about coding. If the question is wrong, just give hints on how to get to the right answer. DO NOT SAY THE RIGHT ANSWER. Just give hints. Be suggestive."}]




import openai
import requests
import json
import sys
from flask import request, jsonify
import json
from firebase_admin import credentials, firestore, initialize_app

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()


with open('Questionbank.json', 'r') as f:
    question_bank = json.load(f)

def get_api_key_from_file(filename):
    with open(filename, 'r') as f:
        api_key = f.read().strip()
    return api_key

openai.api_key = get_api_key_from_file('openaikey.txt')

def interact_with_gpt(user_input, conversation_history, assignment_name):
    # print(assignment_name,"dseds")
    journal_ref = db.collection(assignment_name)
    #journal_ref.add({u'name': u'test', u'added': u'just now'})
    
    context = "The question (only for your context, do not give away answer) is based: " + question_bank[assignment_name] if assignment_name in question_bank else  assignment_name + " Check if user's response is related to this question. If user's response is not related to this question, say it is not related to the question. Do Not give away the answer." #Write a Python function that takes a list of integers as input and returns a new list containing only the unique elements of the original list, maintaining the original order. 
    
    conversation_history.append({"role": "system", "content": context})
    conversation_history.append({"role": "user", "content": user_input})
    

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
        
        # id = request.json['id']
        # journal_ref.document(id).set(request.json)
        # jsonify({"success": True})  
        journal_ref.add({u'My Attempt': user_input, u'Feedback': assistant_response})      
        
        conversation_history.append({"role": "assistant", "content": assistant_response})

        result = {"response": assistant_response}
        return result


conversation_history = [{"role": "system", "content": "You are a GPT-3.5 coding assistant helping with coding questions. Do not give away the right answer to coding questions. DO NOT DO  THAT EVER. Just give feedback to whatever the student asks about coding. If the user input is wrong, just give hints on how to get to the right answer. DO NOT SAY THE RIGHT ANSWER. Just give Hints. Be suggestive. Be vague with the Hints. Do Not give specific Hints to correct the user answer. Do not give away correct answer."}]

