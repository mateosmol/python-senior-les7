import logging
logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w", format="le problemo in yo computadora en %(asctime)s, %(message)s")
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')