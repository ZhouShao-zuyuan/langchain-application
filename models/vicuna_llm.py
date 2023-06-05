from abc import ABC
from langchain.llms.base import LLM
from typing import Optional, List

from models.loader import LoaderCheckPoint
from models.base import (BaseAnswer,
                         AnswerResult)


class VicunaLLM(ABC, BaseAnswer, LLM):

    max_token: int = 10000
    temperature: float = 0.01
    top_p: float = 0.9
    checkPoint: LoaderCheckPoint = None
    history_len: int = 10

    def __init__(self, checkPoint: LoaderCheckPoint):
        super.__init__()
        self.checkPoint = checkPoint
    
    @property
    def _llm_type(self) -> str:
        return 'vicuna'
    
    @property
    def _check_point(self) -> LoaderCheckPoint:
        return self.checkPoint
    
    @property
    def _history_len(self) -> int:
        return self.history_len
    
    def set_history_len(self, history_len: int = 10) -> None:
        self.history_len = history_len
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        # TODO
        pass
    
    def generatorAnswer(self, prompt: str, history: List[List[str]] = [], streaming: bool = False):
        # TODO
        pass