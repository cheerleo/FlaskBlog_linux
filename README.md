# flaskblog_linux
服务器版本的项目代码


使用步骤：
1. 将本项目代码放在/Flask_Blog/flaskblog路径中；
2. 在/Flask_Blog路径下添加run.py，作为启动入口。

run.py文件代码如下：

from flaskblog import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
