# 유스 케이스 입력 객체

import collections

class InvalidRequestObject:
    def __init__(self) -> None:
        self.errors = []

    def add_error(self, parameter: str, message: str) -> None:
        self.errors.append({"parameter": parameter, "message": message})

    def has_errors(self) -> bool:
        return len(self.errors) > 0

    def __bool__(self) -> bool:
        return False                

class ValidRequestObject:
    @classmethod
    def from_dict(cls, adict: dict):
        raise NotImplementedError

    def __bool__(self) -> bool:
        return True
        
# RoomListUseCase 유스 케이스를 위한 요청 객체다.
class RoomListRequestObject(ValidRequestObject):    
    accepted_filters = ["code__eq", "price__eq", "price__lt", "price__gt"]

    def __init__(self, filters: dict=None) -> None:
        """
        There are no validation checks in the __init__ method,
        because this is considered to be an internal method that gets called
        when the parameters have already been validated.
        """
        self.filters = filters

    @classmethod
    def from_dict(cls, adict: dict):
        invalid_req = InvalidRequestObject()

        if "filters" in adict:
            if not isinstance(adict["filters"], collections.Mapping):
                invalid_req.add_error("filters", "Is not iterable")
                return invalid_req

            for key, value in adict["filters"].items():
                if key not in cls.accepted_filters:
                    invalid_req.add_error("filters", "Key {} cannot be used".format(key))
            
        if invalid_req.has_errors():                    
            return invalid_req

        return cls(filters=adict.get("filters", None))


                            

