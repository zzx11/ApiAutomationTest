"""
封装记录日志的方法
"""
import logging
import os
import time


class Logger(object):

    def __init__(self, logger):
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d', time.localtime(time.time()))
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_path = path + '\\Log\\'
        # log_path = r'E:\PythonProject\A_InterfaceTestFramework/Log/'
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger


if __name__ == "__main__":
    log = Logger(logger='TestAdd').get_log()
    log.info("aaaa")
    log.error("bbbb")
    log.debug("bbbb")
