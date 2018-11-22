import time

from common.HTMLTestRunner_PY3 import HTMLTestRunner
from unittest import defaultTestLoader

# 指定测试用例目录
test_dir = './TestCase'
testsuit = defaultTestLoader.discover(test_dir, pattern='test_case.py')

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './Report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='iwherelink系统接口自动化测试',
                            description='运行环境：Windows7, Python3.6, MySQL5.6 ')
    runner.run(testsuit)
    fp.close()