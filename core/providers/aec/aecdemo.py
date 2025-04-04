import gzip
import io
import json
import opuslib_next
import os
import time
import uuid
import wave
import websockets
from typing import Optional, Tuple, List

from config.logger import setup_logging
from core.providers.aec.base import AECProviderBase
import Levenshtein
import queue


class AECProvider(AECProviderBase):
    def check_similar_text(self, output_list: queue.Queue, text: str, session_id: str) -> bool:
        while not output_list.empty():
            item = output_list.get()
            distance = Levenshtein.distance(item, text)
            # 可以设定一个阈值来判断是否相近
            threshold = 10
            if distance <= threshold:
                self.logger.bind(tag=TAG).info(f"-------- {session_id} similar text: {distance}, [{item}], [{text}]")
                return False
            else:
                self.logger.bind(tag=TAG).info(f"-------- {session_id} not --- similar text: {distance}, [{item}], [{text}]")
                return True

