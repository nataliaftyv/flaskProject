from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to PetAdoption!'


@app.route('/Ozzy')
def cat():
    return 'Ozzy'


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')
