import os
from dotenv import load_dotenv
# pip install python-dotenv

import google.generativeai as genai
# pip install -q -U google-generativeai

load_dotenv()

# https://ai.google.dev/tutorials/python_quickstart

class GeminiAI:
    def __init__(self, model_name, instruction, temperature):
        self.model_name = model_name
        self.instruction = instruction
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.temperature = temperature

        genai.configure(api_key=self.api_key)

        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=self.instruction)
        
        self.configure = genai.GenerationConfig(max_output_tokens=2048, temperature=self.temperature, top_p=1, top_k=32)

        self.chat = self.model.start_chat(history=[])

    def generate_response(self, input_text):
        """Generates a response using Gemini model"""
        response = self.model.generate_content(input_text, generation_config=self.configure)
        return response
    
    def send_message(self, input_text):
        response = self.chat.send_message(input_text, generation_config=self.configure)
        return response
    
    def get_history(self):
        history = self.chat.history
        return history
    
    def listar_modelos_gemini(self):
        for model in genai.list_models():
                print(model.name)

        return
