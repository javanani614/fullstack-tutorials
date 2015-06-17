from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')
def index():
    return 'Hello'

@app.route('/hello')
def hello1():
    return render_template('hello.html')

@app.route('/hello/<name>')
def hello2(name):
	#return name
    return render_template('hello_name.html',name=name)

if __name__=='__main__':
    app.run(debug=True)