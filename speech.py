import win32com.client

voice = win32com.client.Dispatch("SAPI.SpVoice")

def say(phrase):
    voice.Speak(phrase)
