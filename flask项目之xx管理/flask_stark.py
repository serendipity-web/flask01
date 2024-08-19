from flask import Flask, request  # 导入Flask库

app = Flask(__name__)  # 创建一个Flask应用实例，__name__代表当前模块的名称


# url与视图
# http://www.qq.com:443/path

@app.route("/")  # 装饰器，告诉Flask当用户访问根路径时应该执行下面定义的index函数
# /表示根路由
def index():  # 定义index函数，处理来自根路径的请求
    return "Hello Flask debug"  # 返回字符串 "Hello World" 给用户


@app.route("/profile/<blog_id>")
def profile(blog_id):
    return f"个人中心{blog_id}"


@app.route('/book/list')
def book_list():
    # 类字典类型
    page = request.args.get("page", default=100, type=int)
    return f"the page is {page}"


if __name__ == '__main__':  # 检查当前模块是否作为主程序运行
    app.run(debug=True, host='0.0.0.0', port=8000)  # 启动Flask的开发服务器，监听请求并响应，默认运行在http://127.0.0.1:5000/
