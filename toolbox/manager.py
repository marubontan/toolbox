from typing import Any, Union
from .base import Either, Right, Left


def Try(fn, obj: Union[Any, Either]) -> Either:
    if type(obj) == Right:
        try:
            return Right(fn(obj.content))
        except Exception as e:
            return Left(e)
    elif type(obj) == Left:
        return obj
    else:
        try:
            return Right(fn(obj))
        except Exception as e:
            return Left(e)
