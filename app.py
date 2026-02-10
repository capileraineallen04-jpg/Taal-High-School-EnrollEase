from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def root():
         return render_template('/index.html')

@app.route('/login')
def login():
         return render_template('/login.html')

@app.route('/signup')
def signup():
         return render_template('/signup.html')

@app.route('/management')
def management():
         return render_template('/management.html')

@app.route('/seniors-form')
def seniors_form():
         return render_template('/seniors_form.html')

@app.route('/juniors-form')
def juniors_form():
         return render_template('/juniors.html')

@app.route('/successfull')
def successfull():
         return render_template('/successfull.html')

if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True)