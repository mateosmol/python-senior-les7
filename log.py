import logging
logging.basicConfig(level=logging.INFO,
                    filename="app.log",
                    format="%(asctime)s - %(levelname)s - %(message)s",)\

import logging

logging.basicConfig(filename='errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        logging.error(f'Division error: {e}')

divide(10, 0)
