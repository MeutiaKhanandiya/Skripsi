from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello! this is the main page <h1>HELLO<h1>"

if __name__ == "__main__":
    app.run()