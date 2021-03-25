from flask import Flask

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'

from blueprint import blueprint
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003, debug=True)