from dataclasses import dataclass
from src.constants import *
import os

CURRENT_DIR = os.getcwd()

@dataclass
class TTSConfig:
    app_name: str = APPLICATION_NAME
    artifact_dir = os.path.join(CURRENT_DIR,app_name,ARTIFACT_DIR_KEY)
    audio_dir = os.path.join(artifact_dir,AUDIO_DIR)
    text_dir = os.path.join(artifact_dir,TEXT_DIR)
