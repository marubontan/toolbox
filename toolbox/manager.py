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


def check_output(output: Either):
    if (not isinstance(output, Either)) or (type(output) is Either):
        raise ValueError("Input type should be subclass of Either.")
    elif type(output) == Right:
        print("SUCCESS")
    else:
        raise output.error
