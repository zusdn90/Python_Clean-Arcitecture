# 데이터 저장소

from abc import ABCMeta, abstractmethod
from typing import List

from rentomatic.domain.entities.room import Room

# 유스케이스 레이어에서는 구체적인 구현이 아닌 인터페이스(추상 클래스)만 정의한다.
class Repository(metaclass=ABCMeta):
    @abstractmethod
    def list(self, filters: dict=None) -> List[Room]:
        pass