import logging
import datetime
logging.basicConfig(filename='/storage/emulated/0/oops2/27-09-2020.txt',level=logging.WARNING,filemode='w')
logging.debug('debug level')
logging.info('info level')
logging.warning('warning level')
logging.error('error level')
logging.critical('critical level')