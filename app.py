from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hare krishna hare krishna krishna krishna hare hare hare rama hare rama rama rama hare hare !"
