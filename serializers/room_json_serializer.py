# 인터페이스 어댑터 레이어는 "프레임워크와 드라이버" 레이어와 "유스 케이스" 레이어 
# 통신 간 필요한 어댑터 모듈들이 위치하는 곳

# "프레임워크와 드라이버" 레이어에서는 REST API로 외부와 데이터를 주고받게 되는데, 
# 이때 json 데이터를 사용한다.

import json

class RoomJsonEncoder(json.JSONEncoder):
    def default(self, o: object):
        try:
            to_serialize = {
                "code": str(o.code),
                "size": o.size,
                "price": o.price,
                "latitude": o.latitude,
                "longitude": o.longitude,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
