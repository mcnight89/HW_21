from typing import Dict

from classes.abstractstorage import Storage
from error import UnknownStorage, InvalidRequest


class Request:
    def __init__(self, request_str: str, storages: Dict[str, Storage]):
        split_request = request_str.lower().split(' ')
        if len(split_request) != 7:
            raise InvalidRequest

        self.amount = int(split_request[1])
        self.product = split_request[2]
        self.destination = split_request[6]
        self.departure = split_request[4]

        if self.destination not in storages or self.departure not in storages:
            raise UnknownStorage
