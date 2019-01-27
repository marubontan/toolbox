import pytest
from toolbox.base import Right, Left
from toolbox.manager import Try, check_output


def test_Try():
    normal_obj = 2
    right_obj = Right(2)
    left_obj = Left(Exception("error_1"))

    def fn_1(obj):
        return obj * 2

    normal_output = Try(fn_1, normal_obj)
    right_output = Try(fn_1, right_obj)
    left_output = Try(fn_1, left_obj)

    assert isinstance(normal_output, Right)
    assert isinstance(right_output, Right)
    assert isinstance(left_output, Left)

    assert normal_output.content == Right(4).content
    assert right_output.content == Right(4).content
    with pytest.raises(Exception):
        raise left_output.error
    assert str(left_output.error) == "error_1"

    def fn_2(obj):
        raise Exception("error_2")

    normal_error = Try(fn_2, normal_obj)
    right_error = Try(fn_2, right_obj)
    left_error = Try(fn_2, left_obj)

    assert isinstance(normal_error, Left)
    assert isinstance(right_error, Left)
    assert isinstance(left_error, Left)

    with pytest.raises(Exception):
        raise normal_error.error
    assert str(normal_error.error) == "error_2"

    with pytest.raises(Exception):
        raise right_error.error
    assert str(right_error.error) == "error_2"

    # the exception from the prior phase should not be overwritten
    with pytest.raises(Exception):
        raise left_error.error
    assert str(left_error.error) == "error_1"


def test_check_output():
    normal_obj = 2
    right_obj = Right(2)
    left_obj = Left(Exception("error_1"))
    with pytest.raises(ValueError):
        check_output(normal_obj)

    try:
        check_output(right_obj)
    except Exception as e:
        pytest.fail("Right object must not raise error.")
        raise e

    with pytest.raises(Exception, match="error_1"):
        check_output(left_obj)
