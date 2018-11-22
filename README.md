
介绍：
  本项目为接口自动化测试框架: unittest + request + excel + htmlTestRunner

  它包含功能:
  * 测试数据初始化，并对数据的插入做了封装。
  * unittest单元测试框架运行测试
  * 支持不同类型接口，cookie和token自动获取并传参
  * 支持不同方式的参数断言，全匹配、状态码、包含
  * 参数解密加密
  * excel格式用例解析读取，回填测试结果
  * ddt实现用例参数化，同一方法执行不同参数的用例
  * HTMLTestRunner生成接口测试报告
  * 测试报告邮件发送

项目结构：
common:通用代码包，封装日志、发送邮件、读取用例数据等
    --assertion.py  断言方法模块
    --consts.py     全局变量模块
    --email.py      邮件设置模块
    --excel_toll.py excel读取数据模块
    --hash.py       加密解密模块
    --logger.py     日志自定义模块
    --request.py    请求类型封装模块
    --session.py    获取cookie、token通用变量模块
    --testlink-data.py  获取testlink上测试用例
config:配置文件包
    --config.ini    接口地址参数配置文件
    --db_config.ini 数据库连接参数配置文件
    --config.py     配置文件读取模块
database:数据库操作包
    --mysql_db.py   mysql数据库连接模块
    --inster_data.py    数据表处理模块
testcase:存放各个项目的用例执行文件
    --test-*.py 用例执行模块
files:存放excel数据
log:存放日志文件
report:存放报告文件
run_main.py 主程序运行入口

Python版本与第三方依赖库：
  * python3.5+ :https://www.python.org/
  * Requests : https://github.com/kennethreitz/requests
  * PyMySQL : https://github.com/PyMySQL/PyMySQL
  * TestLink-API-Python-client 0.8.0
  * xlrd : 
  * addict : 
  * requests_toolbelt : 
  * addict : 
  * ddt
  