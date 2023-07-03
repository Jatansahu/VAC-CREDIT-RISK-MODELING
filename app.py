from flask import Flask, render_template
from waitress import serve

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/style.css')
# def index():
#     return ('style.html')


if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)r
    app.run(debug=True)


# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "<h1>Hello!</h1>"

# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)