from datetime import datetime
import os

def get_current_time():
    fmt = "%Y-%m-%d %H%M%S"
    return f"{datetime.now().strftime(fmt)}"

ROOT_DIR = os.getcwd()
CURRENT_TIME_STAMP = get_current_time()

APPLICATION_NAME = 'src'
ARTIFACT_DIR_KEY = 'artifact'
AUDIO_DIR = 'tts_audio'
TEXT_DIR = 'tts_text'
TEXT_FILE_NAME = 'input_texts.txt'