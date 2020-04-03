from flask import Flask
app = Flask(__name__)

# 如果访问根目录 '/'，返回 Index Page
@app.route('/')
def index():
    return 'Index Page'

# 如果访问 '/hello'，返回 Hello，world!
@app.route('/hello')
def hello():
    return 'Hellp,World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # 显示用户名
    return 'User {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 显示提交整型的用户“id”的结果，注意 "int" 是将输入的字符串形式转为整型数据
    return 'Post {}'.format(post_id)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # 显示 /path/ 之后的路径名
    return 'Subpath {}'.format(subpath)

@app.route('/projects/')
def projects():
    return "The peoject page"

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_from()

def do_the_login():
    return 'Welcome {}'.format('Admin')

def show_the_login_from():
    return 'this is login page'


@app.route('/show_name/<string:username>')
def show_name(username):
    return 'Welcome {}'.format(username)

@app.route('/sum/<int:a>/<int:b>')
def sumab(a, b):
    return '{} + {} = {}'.format(a, b, a+b);


