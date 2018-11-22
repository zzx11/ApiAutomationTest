"""
读取配置文件中参数
"""
from configparser import ConfigParser
import os


class Config:
    # titles:
    ENVIRONMENT_INFO = "environment_info"
    EMAIL = "mail"

    # values:
    # [debug\release]
    VALUE_TESTER = "tester"
    VALUE_ENVIRONMENT = "environment"
    VALUE_VERSION_CODE = "versionCode"
    VALUE_LOGIN_IF = "login_if"
    VALUE_HOST = "host"
    VALUE_LOGIN_HOST = "loginHost"
    VALUE_LOGIN_INFO = "loginInfo"

    # [mail]
    VALUE_SMTP_SERVER = "smtp_server"
    VALUE_SENDER = "sender"
    VALUE_RECEIVER = "receiver"
    VALUE_PSW = "psw"

    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.xml_report_path = Config.path_dir + '/Report/xml'
        self.html_report_path = Config.path_dir + '/Report/html'

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.conf_path, encoding='utf-8')

        self.tester = self.get_conf(Config.ENVIRONMENT_INFO, Config.VALUE_TESTER)
        self.environment = self.get_conf(Config.ENVIRONMENT_INFO, Config.VALUE_ENVIRONMENT)
        self.versionCode = self.get_conf(Config.ENVIRONMENT_INFO, Config.VALUE_VERSION_CODE)
        self.login_if = self.get_conf(Config.ENVIRONMENT_INFO, Config.VALUE_LOGIN_IF)
        self.host = self.get_conf(Config.ENVIRONMENT_INFO, Config.VALUE_HOST)
        self.loginHost = self.get_conf(Config.ENVIRONMENT_INFO, Config.VALUE_LOGIN_HOST)
        self.loginInfo = self.get_conf(Config.ENVIRONMENT_INFO, Config.VALUE_LOGIN_INFO)

        self.smtpserver = self.get_conf(Config.EMAIL, Config.VALUE_SMTP_SERVER)
        self.sender = self.get_conf(Config.EMAIL, Config.VALUE_SENDER)
        self.receiver = self.get_conf(Config.EMAIL, Config.VALUE_RECEIVER)
        self.psw = self.get_conf(Config.EMAIL, Config.VALUE_PSW)

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)
