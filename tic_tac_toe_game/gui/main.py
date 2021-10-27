# -*- coding: utf-8 -*-
"""
   Implements entry point
"""

from controller import Controller


if __name__ == '__main__':
    controller = Controller()
    controller.view.run_loop()
    controller.logger.info('Start game')
