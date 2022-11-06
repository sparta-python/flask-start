from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Flask"


@app.route("/hiraizumi")
def hiraizumi():
    return "じゃけえ、じゃけえ！"


@app.route("/user/<name>")
def heyName(name):
    return name


@app.route("/user/age/<age>")
def Age(age):
    return age


@app.route("/user/<name>/<age>")
def Name_Age(name, age):
    return name + age


@app.route("/html")
def html():
    # return "<h1>Hello 伴地さん</h1>"
    return render_template("index.html")


@app.route("/html/<aaa>")
def htmlName(aaa):
    return render_template("name.html", bbb=aaa)


@app.route("/html/age/<age>")
def htmlAge(age):
    return render_template("age.html", age=age)


@app.route("/query")
def query():
    ccc = request.args.get("aaa")
    return ccc


# http://192.168.40.50:5000/query?aaa=bbb

# 制限しないと意図していないときにflaskが起動してしまうため
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
