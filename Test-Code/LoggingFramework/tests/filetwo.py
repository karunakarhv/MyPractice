from common.logger_util import Logger
import time
import os

def main():

    fileName = os.path.basename(__file__)
    logger = Logger(name=os.path.basename(__file__))
    for i in range(10):
        time.sleep(i)
        logger.info('Hi {}'.format(1))
        logger.debug('How are you? {}'.format('testing'))
        logger.warning('Exceptional warning {}'.format(fileName))
        logger.error('Exceptional error')

main()