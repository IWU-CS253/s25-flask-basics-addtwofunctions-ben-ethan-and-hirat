# calc.py
import math


def calculate(current_value, num, clear):
    if clear:
        return ''  # Clear the current value if clear button is pressed
    elif num:
        if num == '=':
            # Calculate result if '=' is pressed
            try:
                # Safely evaluate the current expression
                return str(eval(current_value))
            except:
                return 'Error'
        elif num == '√':
            # calculate the result if "√" is pressed
            try:
                return str(math.sqrt(float(current_value)))  # return the square root of it
            except:
                return 'Error'
        elif num == '!':
            # calculate the factorial if "!" is pressed
            try:
                return str(math.factorial(int(current_value)))   # return the factorial of the number
            except:
                return 'Error'
        else:
            # Append the pressed button value to the current value
            return current_value + num
    return current_value

