# Controller는 요청에 대해 적합한 유스 케이스로 라우팅 한다.
#이 과정 중에 인터페이스 어댑터 레이어의 Encoder를 이용하여 외부 요청을 유스 케이스에 맞게 변환하고, 
# 유스 케이스로부터의 출력을 외부 응답에 맞게 변환한다.

import json

from flask import Blueprint, Response, request

from rentomatic.repository import mongorepo as mr
from rentomatic.domain.request_objects import room_list_request_object as req
from rentomatic.domain.response_objects import response_objects as res
from rentomatic.serializers import room_json_serializer as ser
from rentomatic.domain.use_cases import room_list_use_case as uc

blueprint = Blueprint("room", __name__)

# response_object의 type -> http response type 을 정의
STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: 200,
    res.ResponseFailure.RESOURCE_ERROR: 404,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500,
}

# repository 에 주입시켜줄 데이터베이스 정보
connection_data = {
    "dbname": "rentomaticdb",
    "user": "root", 
    "password": "rentomaticdb", 
    "host": "localhost"
}