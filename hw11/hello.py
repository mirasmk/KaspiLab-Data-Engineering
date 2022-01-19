from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hell')
def hell():
    return 'Hell'

if __name__ == '__main__':
  app.run()
