import os
import json

# 环境变量（windows设置）
# 【作用】将一些敏感的数值添加到环境变量中，是为了保密，使其不直接在代码中展示出来
# 【添加】系统属性 --> 高级 --> 环境变量 --> ASUS的用户变量处手动新建
# 【提取】使用os.environ.get()获取提前添加环境变量值
# 【注意】新添加的环境变量需要重启之后，才能获取到值！！！！！


# 在服务器中，我们需要json.load方法读取储存在config.json文件中的环境变量
with open("/etc/config.json") as config_file:
	config_dict = json.load(config_file) # 这里获得的config是个字典

class Config:

    # （1）创建RegistrationForm()时候必须要有。A secret key is required to use CSRF.
    # 具体的值已经提前手动添加到系统环境变量（服务器上的/etc/config.json）中
    SECRET_KEY = config_dict.get('SECRET_KEY')

    # （2）定义一个轻量级数据库的地址URI
    # 具体的值已经提前手动添加到系统环境变量（服务器上的/etc/config.json）中
    SQLALCHEMY_DATABASE_URI = config_dict.get('SQLALCHEMY_DATABASE_URI')

    # （3）自动发送验证邮件的邮箱配置
    MAIL_SERVER = "smtp.qq.com"
    MAIL_PORT = 465                      # SSL加密方式对应的端口
    MAIL_USE_SSL = True                  # qq邮箱需要SSL加密方式
    MAIL_USE_TLS = False
    MAIL_USERNAME = config_dict.get('MAIL_USERNAME')
    MAIL_PASSWORD = config_dict.get('MAIL_PASSWORD')
