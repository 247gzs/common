# -*- coding: utf-8 -*-
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger()

if __name__ == '__main__':
    logger.info('test logger')
