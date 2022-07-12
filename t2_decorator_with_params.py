import time
import logging
from random import choice

EAGLE_AND_TAILS = (0, 1)

logger = logging.getLogger('__name__')
logging.basicConfig(level=logging.INFO)

class run_with_delay(object):

    def __init__(self, call_count:int, start_sleep_time: int, factor: int, border_sleep_time: int):
        self.call_count = call_count
        self.start_sleep_time = start_sleep_time
        self.factor = factor
        self.border_sleep_time = border_sleep_time

    def __call__(self, func):
        def wrapped_f(*args):
            t = self.start_sleep_time 
            logger.info('Начало работы')
            for n in range(1, self.call_count + 1):
                if t < self.border_sleep_time:
                    t = self.start_sleep_time * self.factor ** n
                else:
                    t = self.border_sleep_time
                logger.debug(t)
                time.sleep(t)
                result = func(*args)
                logger.info('Запуск номер %s. Ожидание: %s.'
                    ' Результат декорируемой фунцкии = %s' % (n, t, result))
            logger.debug('Конец работы')
        return wrapped_f


@run_with_delay(call_count=10, start_sleep_time=1, factor=2, border_sleep_time=60)
def cast_lots():
    return choice(EAGLE_AND_TAILS)


if __name__ == '__main__':
    cast_lots()