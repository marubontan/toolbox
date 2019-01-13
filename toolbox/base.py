from typing import Any
class Either:
    pass


class Right(Either):
    def __init__(self, content: Any):
        self.content = content


class Left(Either):
    def __init__(self, error):
        self.error = error
