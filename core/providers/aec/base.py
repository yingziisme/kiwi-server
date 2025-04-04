from abc import ABC, abstractmethod
from typing import Optional, Tuple, List

from config.logger import setup_logging
import queue

TAG = __name__
logger = setup_logging()


class AECProviderBase(ABC):


    @abstractmethod
    def check_similar_text(self, output_list: queue.Queue, text:str, session_id: str) -> bool:
        """解码Opus数据并保存为WAV文件"""
        pass

