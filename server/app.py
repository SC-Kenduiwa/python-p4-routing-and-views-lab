#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return '''
    <h1>Python Operations with Flask Routing and Views</h1>
    '''

# Print string route
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print the string in the console
    return parameter  # Display the string in the web browser

# Count route
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = [str(i) for i in range(parameter)]
    return '<br>'.join(numbers)  # Display numbers on separate lines

# Math operations route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero!'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Unsupported operation!'
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
