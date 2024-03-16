from flask import Flask, render_template, request
import openai
import traceback
 
# app = Flask(__name__)
 
class ProgramGeneratorEngine:
    def __init__(self):
        self.response = None
        self.q_nos = None
        self.file_path = None
        self.req_log = None
        self.engine = "gpt-3.5-turbo"  # Assuming 'gpt-3.5-turbo' as default engine
        self.conversation_history = [{"role": "system", "content":"You are an assignments generator for coding questions in python. You will only generate coding questions based on a given topic. The topic should only be python programming related. Provide only the question, no code. Provide only 1 test case"}]
 
        # Set your OpenAI API key here
        openai.api_key = self.get_api_key_from_file('openaikey.txt')

    def get_api_key_from_file(self,filename):
        with open(filename, 'r') as f:
            api_key = f.read().strip()
        return api_key
 
    def train_model(self):
        tokens = 300
        params = {'model': self.engine,
                  'messages': self.conversation_history,
                  'max_tokens': tokens
                  }
        # try:
        # self.response = openai.ChatCompletion.create(**params)
        self.response = openai.chat.completions.create(**params)
        # except openai.error.OpenAIError as error:
        #     print(f"OpenAI Error: {error}")
        #     return False
        # except Exception as error:
        #     print(f"Error sending OpenAI request: {error}")
        #     traceback.print_exc()
 
        if not self.response:
            print("GPT None response during training")
            return False
 
        return True
 
    def generate_questions(self, prompt, difficulty_level):
        tokens = 1000
        self.conversation_history.append({"role": "user", "content": f"Change the topic to: {prompt}"})
        
        # Adjust the difficulty level based on user input
        difficulty_modifier = ""
        if difficulty_level.lower() == "easy":
            difficulty_modifier = "easy"
        elif difficulty_level.lower() == "medium":
            difficulty_modifier = "medium"
        elif difficulty_level.lower() == "hard":
            difficulty_modifier = "hard"
 
        messages = self.conversation_history + [{"role": "user", "content": f"Difficulty: {difficulty_modifier}"}]
        
        params = {'model': self.engine,
                  'messages': messages,
                  'max_tokens': tokens,
                  'temperature': 0.3
                  }
        # try:
        #self.response = openai.ChatCompletion.create(**params)
        self.response = openai.chat.completions.create(**params)


        # except openai.error.OpenAIError as error:
        #     print(f"OpenAI Error: {error}")
        #     return False
        # except Exception as error:
        #     print(f"Error sending OpenAI request: {error}")
        #     traceback.print_exc()
 
        if not self.response:
            print("GPT None response during question generation")
            return False
 
        assistant_response = self.response.choices[0].message.content.strip()
        self.conversation_history.append({"role": "assistant", "content": assistant_response})
 
 
        return assistant_response