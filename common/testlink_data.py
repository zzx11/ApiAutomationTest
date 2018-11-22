import re

import testlink


class Export(object):

    def __init__(self,project_name):
        self.project_name = project_name

    def export_test_case(self):

        url = 'http://localhost/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
        key = '2370ebb0b852cfa4f4b557c0d7001220'
        tlc = testlink.TestlinkAPIClient(url, key)

        tc_lis = []
        project_id = tlc.getProjectIDByName(self.project_name)

        for data in tlc.getFirstLevelTestSuitesForTestProject(project_id):
            id1 = data['id']
            name1 = data['name']
            for data in tlc.getTestCasesForTestSuite(id1, True, 'full'):
                name = data["name"]
                external_id = data["external_id"]
                importance = data["importance"]
                execution_type = data["execution_type"]
                author = data["author_id"]

                for i in range(len(data["steps"])):
                    tc_dic = {}
                    steps = data["steps"][i]["actions"]
                    except_result = data["steps"][i]["expected_results"]
                    step_str = str(steps)
                    except_result_str = str(except_result).replace('<p>', "").replace('</p>', "").replace('\n',"")
                    method = re.search('(([\u8bf7\u6c42\u7c7b\u578b]+：).+?(?=</p))', step_str).group(1).replace('请求类型：',
                                                                                                                "")
                    url = re.search('(([\u8bf7\u6c42\u5730\u5740]+：).+?(?=</p))', step_str).group(1).replace('请求地址：',
                                                                                                             "")
                    data = re.search('(([\u8bf7\u6c42\u53c2\u6570]+：).+?(?=</p))', step_str).group(1).replace('请求参数：',
                                                                                                              "").replace(
                        '&#39;', "'")
                    tc_dic['Model'] = name1
                    tc_dic['Case'] = name
                    tc_dic['Num'] = external_id
                    tc_dic['Importance'] = self.format_importance(importance)
                    tc_dic['Method'] = method
                    tc_dic['Url'] = url
                    tc_dic['Data'] = data
                    tc_dic['Expect'] = except_result_str
                    tc_lis.append(tc_dic)
        return tc_lis

    def format_execution_type(self, source_data):
        switcher = {
            '2': "自动化",
            '1': "手工"
        }
        return switcher.get(source_data, "Param not defind")

    def format_importance(self, source_data):
        switcher = {
            '1': "低",
            '2': "中",
            '3': "高"
        }
        return switcher.get(source_data, "Param not defind")

    def format_auth(self, source_data):
        switcher = {
            '1': "admin",
        }
        return switcher.get(source_data, "Param not defind")


if __name__ == '__main__':

    dp = Export('iWhereLinkApi')
    lis = dp.export_test_case()
    print(lis)
