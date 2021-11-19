import pytest


def is_sub_str(str1, str2):
    if (str1.find(str2) == -1):
        pytest.fail()