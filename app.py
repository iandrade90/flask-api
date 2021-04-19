from flas import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Gabriel Alejandro'

if __name__ == "__main__":
    app.run()
