from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('//akanksha_cal')
def cal_page():
    return render_template('index.html')

@app.route("/math", methods = ['POST'])
def calculator_test():
    ops = request.form['operation']
    first_num = float(request.form['num1'])
    second_num = float(request.form['num2'])

    if ops == 'add':
        r = first_num + second_num
        return f"Addition of {first_num} and {second_num} is {r}"
    
    if ops == 'subtract':
        r = first_num - second_num
        return f"Subtraction of {first_num} and {second_num} is {r}"
    
    if ops == 'mul':
        r = first_num * second_num
        return f"Multiplication of {first_num} and {second_num} is {r}"
    
    if ops == 'div':
        r = first_num / second_num
        return f"Division of {first_num} and {second_num} is {r}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
