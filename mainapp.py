from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import openai
import os

app = Flask(__name__)
socketio = SocketIO(app)

# Set your OpenAI API key
openai.api_key = os.getenv('Chatbot_Key')

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    user_message = data['message']
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=user_message,
        max_tokens=150
    )
    bot_response = response.choices[0].text.strip()
    emit('response', {'reply': bot_response})

if __name__ == '__main__':
    socketio.run(app, debug=True)
