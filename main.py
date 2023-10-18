from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://esp-amrit-umajin.000webhostapp.com/your_endpoint"
    response = requests.get(url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)