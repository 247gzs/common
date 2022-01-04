# -*- coding: utf-8 -*-
import calendar
import time
from datetime import date, datetime, timedelta


def now() -> datetime:
    return datetime.now()


def timestamp(dt: datetime = None) -> int:
    """
    获取时间戳

    单位： 毫秒
    """
    if dt:
        return int(dt.timestamp() * 1000)
    return int(time.time() * 1000)


def weekday(dt: datetime) -> int:
    """
    获取指定日期是星期几（1-7）
    """
    return dt.weekday() + 1


def today() -> date:
    """
    获取当前天的日期
    """
    return date.today()


def today2int() -> int:
    """
    日期转int
    """
    today_date = date.today()
    return today_date.year * 10000 + today_date.month * 100 + today_date.day


def today2str(str_format="%Y%m%d") -> str:
    """
    日期转字符串
    """
    return today().strftime(str_format)


def date2int(dt: datetime) -> int:
    """
    日期转int
    """
    return dt.year * 10000 + dt.month * 100 + dt.day


def date2str(dt: datetime, str_format="%Y-%m-%d") -> str:
    """
    日期转字符串
    """
    return dt.strftime(str_format)


def create_date(year: int, month: int, day: int) -> datetime:
    """
    创建日期
    """
    return datetime(year, month, day)


def date_delta(start_date: datetime, end_date: datetime) -> int:
    """
    计算日期差值

    NOTE 可能出现负数
    """
    return (end_date - start_date).days


def seconds_delta(start_date: datetime, end_date: datetime) -> int:
    """
    计算秒差值
    """
    return (end_date - start_date).seconds


def date_by_delta(dt: datetime, **kwargs) -> datetime:
    """
    对日期对象进行偏移

    kwargs 中存储的是偏移的时间
        相关取值: days、seconds、minutes、hours、weeks等等
    """
    return dt + timedelta(**kwargs)


def how_many_days(year: int, month: int) -> int:
    """
    获取某年某月一共有多少天
    """
    _, days = calendar.monthrange(year, month)
    return days


def quarter(dt: datetime) -> int:
    """
    获取指定日期是第几季度
    """
    month = dt.month

    return month // 3


def quarter_start_date(dt: datetime) -> datetime:
    """
    获取指定日期所属季度的第一天
    """
    return create_date(
        dt.year,
        ((quarter(dt) + 2) // 3 - 1) * 3 + 1,
        1
    )


def quarter_end_date(dt: datetime) -> datetime:
    """
    获取指定日期所属季度的最后一天
    """
    month = quarter(dt) * 3
    return create_date(
        dt.year,
        month,
        how_many_days(dt.year, month)
    )


def weekday_in_interval(
        day: int, start_date: datetime, end_date: datetime, case_func=str, format='%Y%m%d',
) -> list:
    """
    获取给定区间内的一周的第几天

    :param format: 当case_func 指定为str时，用于格式化的模式
    :param case_func: 指定返回数据的类型（datetime、str）
    """
    item_list = []
    while start_date <= end_date:
        if weekday(start_date) == day:
            if case_func == datetime:
                item_list.append(start_date)
            else:
                item_list.append(start_date.strftime(format))
        start_date = date_by_delta(start_date, days=1)
    return item_list


def week_in_year(dt: datetime) -> int:
    """
    返回指定日期是一年的第几周
    """
    return dt.isocalendar()[0]


def day_in_year(dt: datetime) -> int:
    """
    获取指定日期是那一年的第几天
    """
    month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(dt.year):
        month_day[1] = 29
    return sum(month_day[:dt.month - 1]) + dt.day


def is_leap_year(year) -> bool:
    """
    判断给定年份是否是闰年
    """
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


if __name__ == '__main__':
    from methods.logger import logger

    logger.info(today2int())
    logger.info(timestamp())
    logger.info(weekday_in_interval(5, datetime(2021, 10, 1), datetime(2021, 12, 29)))
    logger.info(weekday_in_interval(5, datetime(2021, 10, 1), datetime(2021, 12, 29), case_func=datetime))
