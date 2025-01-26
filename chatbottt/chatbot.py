import google.generativeai as genai
import os

# Replace with your actual Gemini API key
API_KEY = "AIzaSyDPsmrIvWcgEMYP7Sgf7SKvzKy704-g3s4" # Set your API key as an environment variable instead for better security

genai.configure(api_key=API_KEY)

# Select the Gemini model
model = genai.GenerativeModel('gemini-pro')

def generate_response(prompt, history=[]):
    """Generates a response from the Gemini model.

    Args:
        prompt (str): The user's input prompt.
        history (list): A list of previous conversation turns (optional).

    Returns:
        str: The generated response from the model.
    """
    
    chat = model.start_chat(history=history)
    response = chat.send_message(prompt)
    return response.text

def chatbot_loop():
    """Runs the main chatbot loop."""
    history = []  # Initialize conversation history

    print("Chatbot: Hi there! I'm a Gemini-powered chatbot. How can I help you?")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        # Pass conversation history to model
        response = generate_response(user_input, history=history)
        print(f"Chatbot: {response}")
        history.append({'role': 'user', 'parts': [user_input]})
        history.append({'role': 'model', 'parts': [response]})
       

if __name__ == "__main__":
    chatbot_loop()