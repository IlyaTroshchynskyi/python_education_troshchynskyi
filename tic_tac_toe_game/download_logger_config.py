# -*- coding: utf-8 -*-
"""
   Read config from yaml file
"""


import logging.config
import yaml


def set_config_logger():
    """
    Read and set configuration for logger from config file
    """

    with open('config_logger.yaml', 'r') as file:
        config = yaml.safe_load(file.read())
        logging.config.dictConfig(config)

    logger = logging.getLogger(__name__)
    return logger
