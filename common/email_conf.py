"""
封装发送邮件的方法
"""
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.logger import Logger
from config import config

report_path = 'E:\\PythonProject\\A_InterfaceTestFramework\\Report\\html\\'  # 测试报告的路径

logger = Logger(os.path.basename(__file__))
conf = config.Config()


class SendMail(object):

    def get_report(self):  # 该在测试报告的路径下找到最新的测试报告
        """获取最新的测试报告"""
        lists = os.listdir(report_path)
        lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
        # 找到最新生成的报告文件
        report_file = os.path.join(report_path, lists[-1])
        return report_file

    def send_mail(self, title):
        '''发送最新的测试报告内容'''
        # 读取测试报告的内容
        with open(self.get_report(), "rb") as f:
            mail_body = f.read()
        # 定义邮件内容
        msg = MIMEMultipart()
        body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg['Subject'] = title
        msg["from"] = conf.sender
        msg["to"] = conf.receiver
        # 加上时间戳
        # msg["date"] = time.strftime('%a, %d %b %Y %H_%M_%S %z')
        msg.attach(body)
        # 添加附件
        att = MIMEText(open(self.get_report(), "rb").read(), "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename= "report.html"'
        msg.attach(att)
        # 登录邮箱
        smtp = smtplib.SMTP()
        # 连接邮箱服务器
        smtp.connect(conf.smtpserver)
        # 用户名密码
        smtp.login(conf.sender, conf.psw)
        smtp.sendmail(conf.sender, conf.receiver, msg.as_string())
        smtp.quit()
        print('test report email has send out !')


if __name__ == '__main__':
    sm = SendMail()
    sm.send_mail('接口自动化测试报告')
