from elevenlabs import ElevenLabs

client = ElevenLabs(api_key="sk_7c42c228e164b3297903f4bcb893331bbc81e4b669b60304")

voices = client.voices.get_all()

for v in voices.voices:
    print(v.voice_id, "-", v.name)


