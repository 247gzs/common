# -*- coding: utf-8 -*-
from functools import wraps

from methods.dt import now
from methods.logger import logger


def decorate(f):
    @wraps(f)
    def func(*args, **kwargs):
        func_name = f.__name__
        logger.info(f"function={func_name}\tstart_time={now()}")
        res = f(*args, **kwargs)
        logger.info(f"function={func_name}\tend_time={now()}")
        return res
    return func


if __name__ == '__main__':
    @decorate
    def test_decorate():
        pass

    test_decorate()
