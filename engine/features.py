import playsound as playsound
import eel
import os
from engine.command import * 
from engine.config import *
import pywhatkit as kit
import re
# Start Sound Player Function

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound.playsound(music_dir) 

@eel.expose
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query != "":
        speakFunction("Opening "+query)
        os.system('start '+query)
    else:
        speakFunction("not found")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speakFunction("Playing "+search_term+" on Youtube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\syoutube'
    # Use re.search to find the match in command 
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match found, return the extracted song name; otherwise, return None
    return match.group(1) if match else None