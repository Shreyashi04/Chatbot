import google.generativeai as genai
from dotenv import load_dotenv

# Set up your API key
genai.configure(api_key="AIzaSyDtw-OryF3PLRyMsnA08jMPD5gz07L0MqY")

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

def chat_with_gemini():
    print("Gemini Chatbot (type 'exit' to stop)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = model.generate_content(user_input)
        print("Chatbot:", response.text)

# Run chatbot
chat_with_gemini()