import sys
import os 
import base64
import datetime
from src.constants import *
from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import TTSConfig
from gtts import gTTS

class TTSApplication():
    def __init__(self,app_config=TTSConfig()):
        try:
            self.app_info = app_config
            self.artifact_dir = self.app_info.artifact_dir
            self.audio_dir = self.app_info.audio_dir
            self.text_dir = self.app_info.text_dir
            logging.info(f"Loaded all application configurations")
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def texttospeech(self,text,accent):
        try:
            my_text = text
            text_dir = self.text_dir
            text_filename = TEXT_FILE_NAME
            text_file_path = os.path.join(text_dir,text_filename)
        
            with open(text_file_path,"a+") as f:
                f.write(f"\n{my_text}")

            tts = gTTS(my_text,lang='en',tld=accent,slow=False)

            filename = f"converted_file{CURRENT_TIME_STAMP}.mp3"
     
            audio_dir = self.audio_dir

            if not os.path.exists(audio_dir):
                os.makedirs(audio_dir, exist_ok=True)
                
            audio_path = os.path.join(audio_dir,filename)
            tts.save(audio_path)

            with open(audio_path,"rb") as file:
                str = base64.b64encode(file.read())

            return str 

        except Exception as e:
            raise CustomException(e,sys)

