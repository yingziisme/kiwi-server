import time
import io
import wave
import os
from typing import Optional, Tuple, List
import uuid
import websockets
import json
import gzip

import opuslib_next
import queue
from core.providers.aec.base import AECProviderBase

from config.logger import setup_logging

TAG = __name__
logger = setup_logging()


class AECProvider(AECProviderBase):

    def check_similar_text(self, output_list: queue.Queue, text:str, session_id: str) -> bool:

        return False
