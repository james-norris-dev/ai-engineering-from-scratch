from flask importt Flask

app = Flask(__name__)

@app.roue("/")
def hello():
    return "Hello from ai-dev container!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50000)