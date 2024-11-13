from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import TTSConfig
import sys
import os 

from src.constants import TEXT_FILE_NAME, CURRENT_TIME_STAMP
from gtts import gTTS

class TTSApplication():
    def __init__(self,app_config=TTSConfig()) -> None:
        try:
            self.app_config = app_config
            self.artifact_dir = app_config.artifact_dir
            self.audio_dir = app_config.audio_dir
            self.text_dir = app_config.text_dir
        except Exception as e:
            raise CustomException(e,sys)
        
    def texttospeech(self,text,accent):
        try:
            text_filename = TEXT_FILE_NAME
            text_file_path = os.path.join(self.text_dir,TEXT_FILE_NAME)
            text_file_path = os.makedirs(self.text_dir,exist_ok=True)
            with open(text_file_path,'a+') as f:
                f.write(f"\n{text}")

            tts = gTTS(text,lang='en',tld=accent,slow=False)

            filename = f"converted_file{CURRENT_TIME_STAMP}.mp3"
            os.makedirs(self.audio_dir,exist_ok=True)
            audio_path = os.path.join(self.audio_dir,filename)
            tts.save(audio_path)

            with open(audio_path,"rb") as file:
                str = base64.b64encode(file.read())

            return str 

        except Exception as e:
            raise CustomException(e,sys)

