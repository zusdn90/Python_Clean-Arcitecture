# 유스케이스 레이어는 비지니스 로직 그 자체를 담고 있다.

from typing import Union

from rentomatic.domain.interfaces.repository import Repository
from rentomatic.domain.request_objects import room_list_request_object as req
from rentomatic.domain.response_objects import response_objects as res
from rentomatic.domain.response_objects.response_objects import ResponseFailure, ResponseSuccess

class RoomListUserCase:
    def __init__(self, repo: Repository):
        self.repo = repo

    # 유스케이스는 execute()로 실행됨.
    # 유스케이스 입력 - request_object / 출력 - response_object 
    def execute(
        self, request_objects: Union[req.ValidRequestObject, req.InvalidRequestObject]
    ) -> Union[ResponseSuccess, ResponseFailure]:
        if not request_objects:
            return res.ResponseFailure.build_from_invalid_request_object(request_objects)

        try:
            rooms = self.repo.list(filter=request_objects.filters)
            return res.ResponseSuccess(rooms)

        except Exception as exc:
            return res.ResponseFailure.build_system_error("{}: {}".format(exc.__class__.__name__, "{}".format(exc)))
