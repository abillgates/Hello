from flask import *
from testJava import useJava
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Index Page'


@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        a = request.form.get('firstArg')
        b = request.form.get('secondArg')
        a, b = int(a), int(b)
        result = useJava(a, b)
        return Response(str(result))
    else:
        return render_template('login.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    print(name)
    return render_template('hello.html', name=name)


@app.route('/u')
def geturl():
    get_str = request.args.get('info')
    return get_str


@app.route('/j')
def get_data():
    data = {
        'password': '123456',
        'username': 'zhang',
        'address': {
            'city': 'Beijing',
            'street': 'Xueyuanlu',
            'postcode': '10010'
        }
    }
    return jsonify(data)


if __name__ == '__main__':
    #deploy app make visable
    app.run(host='0.0.0.0')
