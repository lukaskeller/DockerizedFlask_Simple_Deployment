from flask import Flask
from flask import request, render_template, redirect
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect('/math')




@app.route('/math/submit', methods=['POST'])
def show_result():
    if request.method == 'POST':
        data = request.form
        print(data)

        res = float(data['val1']) + float(data['val2'])
        return f'Hello! Your result is: {res}'

@app.route('/math', methods=['GET'])
def login():

    if request.method == 'GET':
        return render_template('math.html')





if __name__ == "__main__":
    app.run(host='0.0.0.0')


