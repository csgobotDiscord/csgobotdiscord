"""
Утилита для форматирования времени.
"""

import pendulum
from source.resources.config import config


pendulum.set_locale(name = config["discord"]["interface"]["timelocal"])


def duration_readable(seconds: int) -> str:
    """
    Функция для читаемого формата оставшегося времени
    :param seconds: Количество секунд
    :return: Строка с читаемым форматом времени
    """

    return pendulum.duration(seconds = seconds).in_words()


def timedelta_readable(time: pendulum.datetime) -> str:
    """
    Функция для читаемого формата разницы времени
    :param time: Время
    :return:
    """

    now = pendulum.now()
    time.replace(tzinfo = now.tzinfo)
    delta_seconds: int = (now - time).total_seconds()
    return now.subtract(seconds = delta_seconds).diff_for_humans()


def time_readable(time: pendulum.datetime) -> str:
    """
    Функция для читаемого формата времени
    :param time: Время
    :return: Строка с читаемым форматом времени
    """

    return time.strftime(config["discord"]["interface"]["timeformat"])
