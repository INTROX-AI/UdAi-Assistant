from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
import threading

app = Flask(__name__)

# Set the API key use google Ai Studio to gain an Api key   
api_key = "YOUR_API_KEY"

genai.configure(api_key=api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", # Use the model name from google Ai Studio
    generation_config=generation_config,
    system_instruction='''Do not use emojis in your answers
    Make your responses as small as possible, only give a detailed response and that too not more than 100 words.
    You are an Ai assistant named Udai. Talk friendly cool and calm.

    Only give answers based on this rules
    '''
)

chat_session = model.start_chat(
#CHANGE THE HISTORY TO MAKE THE ASSISTANT MORE SMART ACCORDING TO YOUR NEEDS
  history=[
    {
      "role": "user",
      "parts": ["Hi, you are a virtual assistant",],
    },
    {
      "role": "model",
      "parts": ["Ok, got it",],
    },
    {
      "role": "model",
      "parts": ["Your name is Udai. You are a virtual assistant",],
    },
    {
      "role": "model",
      "parts": ["Ok, noted"],
    }
  ]
)

# Start pyttsx3 TTS engine
tts_engine = pyttsx3.init()
voices = tts_engine.getProperty('voices')
tts_engine.setProperty("voice", voices[0].id)  # Change index for different voices
tts_engine.setProperty("rate", 160)  # Speed of speech
tts_engine.setProperty("volume", 1)
tts_engine.setProperty("pitch", 10)

# Variable which tracks the current audio status
current_audio = None

def synthesize_text(text):
    global current_audio
    if current_audio:
        current_audio.stop()  # Stop any currently playing audio
    tts_engine.save_to_file(text, 'static/response.mp3')
    tts_engine.runAndWait()
    current_audio = pyttsx3.init()
    current_audio.setProperty('voice', tts_engine.getProperty('voice'))
    current_audio.save_to_file(text, 'static/response.mp3')
    current_audio.runAndWait()
    current_audio = None  # Reset current_audio to ensure it doesn't interfere with the next playback

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.json.get('message')
    response = chat_session.send_message(user_input)
    cleaned_response_text = response.text.replace("*", "").replace("#", "")  # Clean the response text
    synthesize_text(cleaned_response_text)  # Use the cleaned text for TTS
    return jsonify({"response": cleaned_response_text})  # Return the cleaned text in the JSON response

def listen_for_input():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    while True:
        with mic as source:
            audio = recognizer.listen(source)
        try:
            user_input = recognizer.recognize_google(audio)
            response = chat_session.send_message(user_input)
            synthesize_text(response.text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == '__main__':
    threading.Thread(target=listen_for_input).start()
    app.run(host="0.0.0.0", debug=True)