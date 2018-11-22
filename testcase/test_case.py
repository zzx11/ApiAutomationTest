import unittest

import ddt

from common import assertion, consts
from common.excel_tool import get_data
from common.logger import Logger
from common.request import Request
from config import config
from database.inster_data import clear_data

datas = get_data('casefile.xlsx')
my_log = Logger(logger='test_case').get_log()
conf = config.Config()


@ddt.ddt
class TestIWhereLink(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        clear_data()
        my_log.info('执行测试前进行数据清理···')

    @ddt.unpack
    @ddt.data(*datas)
    def test_case(self, **args):
        # module,case_name,case_num,case_imp,request_type,request_url,request_param,case_except,case_author
        self.model_name = args.get('Model')
        self.case_name = args.get('Case')

        self._testMethodDoc = self.model_name + '_' + self.case_name  # 单个文件运行时请注释此行

        self.url = args.get('Url')
        self.login_state = args.get('Login_State')
        self.method = args.get('Method')
        self.data = args.get('Data')
        self.status_code = args.get('Status_Code')
        self.expect_type = args.get('Expect_Type')
        self.expect = args.get('Expect')

        test = assertion.Assertions()
        request = Request()

        if self.method == 'post':
            my_log.info("开始执行post请求！模块名称为： %s ，用例名称为 %s" % (self.model_name, self.case_name))
            r = request.post_request(url=self.url, data=self.data, login_state=self.login_state)
            assert test.assert_code(r['code'], self.status_code)
            if self.expect_type == 'body':
                assert test.assert_in_text(r['body'], self.expect)
            elif self.expect_type == 'text':
                assert self.expect in r['text']
            elif self.expect_type == 'time_consuming':
                assert test.assert_in_text(r['time_consuming'], self.expect)
            elif self.expect_type == 'time_total':
                assert test.assert_in_text(r['time_total'], self.expect)
            else:
                my_log.error('excel文件中设置的预期类型不符合格式！')
        elif self.method == 'get':
            my_log.info("开始执行get请求！模块名称为： %s ，用例名称为 %s" % (self.model_name, self.case_name))
            r = request.get_request(url=self.url, data=self.data, login_state=self.login_state)
            assert test.assert_code(r['code'], self.status_code)
            if self.expect_type == 'body':
                assert test.assert_in_text(r['body'], self.expect)
            elif self.expect_type == 'text':
                assert self.expect in r['text']
            elif self.expect_type == 'time_consuming':
                assert test.assert_time(r['time_consuming'], self.expect)
            elif self.expect_type == 'time_total':
                assert test.assert_time(r['time_total'], self.expect)
            else:
                my_log.error('excel文件中设置的预期类型不符合格式！')
        else:
            my_log.error("暂不支持此种请求方式！")

    def test_error(self):
        """ 此用例错误 """
        self.assertEqual(1 / 0, 1)

    def test_py3_fail(self):
        """ 此用例失败 """
        self.assertEqual(1 + 1, 3)

    @unittest.skip('跳过测试')
    def test_py4_skip(self):
        """ 此用例跳过 """
        self.assertEqual(1 + 1, 3)


if __name__ == '__main__':
    unittest.main()
    print(consts.RESULT_LIST)
