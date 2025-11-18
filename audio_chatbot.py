from transformers import pipeline
import sounddevice as sd
from scipy.io.wavfile import write
import assemblyai as aai
from elevenlabs import ElevenLabs
import pygame
import os

# ----------------------------- #
# Initialize chatbot with improved prompt
# ----------------------------- #
chatbot = pipeline("text2text-generation", model="google/flan-t5-base")
print("Chatbot model loaded!")

# ----------------------------- #
# 1. Record Audio
# ----------------------------- #
def record_audio(filename="user_input.wav", duration=5, fs=16000):
    print("Speak now...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, audio_data)
    print("✔ Audio recorded.")
    return filename

# ----------------------------- #
# 2. Speech-to-Text (AssemblyAI)
# ----------------------------- #
def audio_to_text_assemblyai(filename, api_key):
    aai.settings.api_key = api_key
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(filename)
    return transcript.text

# ----------------------------- #
# 3. Generate Chatbot Response with better prompt
# ----------------------------- #
def chat_response(user_text):
    prompt = (
        "You are a knowledgeable and helpful assistant. Answer the user's question as accurately and informatively as possible. "
        "If you don't know the exact answer, provide the best possible response.\n"
        "Question: " + user_text + "\nAnswer:"
    )
    output = chatbot(prompt, max_new_tokens=150, no_repeat_ngram_size=2, temperature=0.7)
    return output[0]['generated_text'].strip()


# ----------------------------- #
# 4. Text-to-Speech (ElevenLabs)
# ----------------------------- #
def text_to_speech_elevenlabs(text, api_key, output="response.mp3"):
    client = ElevenLabs(api_key=api_key)
    audio_stream = client.text_to_speech.convert(
        text=text,
        voice_id="EXAVITQu4vr4xnSDxMaL",
        model_id="eleven_multilingual_v2"
    )

    audio_bytes = b""
    for chunk in audio_stream:
        audio_bytes += chunk

    with open(output, "wb") as f:
        f.write(audio_bytes)

    return output

# ----------------------------- #
# 5. Play Audio
# ----------------------------- #
def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    print("✔ Audio playback finished.")

# ----------------------------- #
#  Main Loop
# ----------------------------- #
def main():
    ASSEMBLYAI_KEY = "1169573ba261431c8104fc6deb3fcb42"
    ELEVENLABS_KEY = "sk_efda595b79ef40f7e72c212d91e02a18f469851b9bbd3bb4"
    print("\nVoice Chatbot Started! Say 'exit' to quit.\n")

    while True:
        try:
            audio_file = record_audio()
            print("Transcribing...")
            user_text = audio_to_text_assemblyai(audio_file, ASSEMBLYAI_KEY)
            print("You said:", user_text)

            if user_text.lower() in ["exit", "quit", "stop"]:
                print("Exiting chatbot.")
                break

            print("Generating reply...")
            bot_reply = chat_response(user_text)
            print("Bot:", bot_reply)

            print("Converting reply to speech...")
            tts_file = text_to_speech_elevenlabs(bot_reply, ELEVENLABS_KEY)

            print("Playing response...")
            play_audio(tts_file)

        except Exception as e:
            print("ERROR:", e)
            break

if __name__ == "__main__":
    main()
