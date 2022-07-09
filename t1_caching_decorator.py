import logging

logging.basicConfig(level=logging.DEBUG)

cached_results = {}

def cached(func):
    def wrapper(number):
        global cached_results
        func_name = func.__name__
        logging.debug('Number %s' % number)
        if (func_name, number) in cached_results:
            logging.debug('Load from cache')
            return cached_results[(func_name, number)]
        logging.debug('Calculate first time')
        calculated_result = func(number)
        cached_results[(func_name, number)] = calculated_result
        return calculated_result
    return wrapper 

@cached
def multiplier(number: int):
    return number * 2

@cached
def add_2(number: int):
    return number + 2

if __name__ == '__main__':
    logging.info(multiplier(2))
    logging.info(multiplier(3))
    logging.info(multiplier(4))
    
    logging.info(multiplier(2))
    logging.info(multiplier(3))
    logging.info(multiplier(4))

    logging.info(add_2(2))
    logging.info(add_2(3))
    logging.info(add_2(4))

    logging.info(add_2(2))
    logging.info(add_2(3))
    logging.info(add_2(4))