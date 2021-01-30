from typing import Dict


# 엔티티는 비지니스 로직의 중요한 데이터를 표한하는 핵심 객체
class Room:
    def __init__(self, code: str, size: int, price: int, longitude: float, latitude: float):
        self.code = code
        self.size = size
        self.price = price
        self.longitude = longitude
        self.latitude = latitude

    @classmethod
    def from_dict(cls, adict: Dict):
        return cls(
            code=adict["code"],
            size=adict["size"],
            price=adict["price"],
            longitude=adict["longitude"],
            latitude=adict["latitude"],
        )

    def to_dict(self):
        return {
            "code": self.code,
            "size": self.size,
            "price": self.price,
            "longitude": self.longitude,
            "latitude": self.latitude,
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
