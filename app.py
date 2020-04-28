from flask import Flask, render_template
from flask import url_for
from flask import redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Bootstrap_Project_Main.html')

@app.route('/Bootstrap_Project_Signup.html')
def signup():
    return render_template('Bootstrap_Project_Signup.html')

if __name__ == '__main__':
    app.run(debug=True)
