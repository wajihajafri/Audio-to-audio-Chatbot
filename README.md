# Audio-to-audio-Chatbot
# Voice Interactive Chatbot

A Python voice-based chatbot application integrating Hugging Face transformers, AssemblyAI speech-to-text, and ElevenLabs text-to-speech APIs. This project enables natural, conversational interaction via voice input and output.

## Features
- Voice recording via microphone.
- Speech-to-text transcription using AssemblyAI API.
- Natural language response generation using `google/flan-t5-base` transformer model.
- Text-to-speech conversion with ElevenLabs API for natural, lifelike voice output.
- Audio playback of chatbot responses.
- Continuous interactive voice loop with exit commands.

## Tech Stack
- Python 3.x
- Hugging Face Transformers (`transformers` library)
- AssemblyAI speech-to-text API
- ElevenLabs text-to-speech API
- sounddevice & scipy (audio recording and saving)
- pygame (audio playback)

## Setup Instructions

1. Clone this repository:

2. Install dependencies:

3. Obtain API keys:
- Get an AssemblyAI API key from 
- Get an ElevenLabs API key from 
4. Update the "main()" function in "chatbot.py" with your API keys:

5. Run the chatbot:

## Usage

- Speak clearly into your microphone when prompted.
- The chatbot will transcribe your speech, generate a response, and speak it back to you.
- Say "exit", "quit", or "stop" to end the conversation.


## Acknowledgments

- Hugging Face for the transformers library.
- AssemblyAI for speech recognition API.
- ElevenLabs for text-to-speech services.
- Pygame for easy audio playback.



