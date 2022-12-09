class BaseError(Exception):
    message = "Неизвестная ошибка"


class NotEnoughSpace(BaseError):
    message = "Недостаточно места"


class UnknownProduct(BaseError):
    message = "Неизвестный товар"


class NotEnoughProduct(BaseError):
    message = "Недостаточно товара"


class InvalidRequest(BaseError):
    message = "Неправильный запрос"


class UnknownStorage(BaseError):
    message = "Неизвестный склад"
