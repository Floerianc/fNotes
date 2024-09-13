import math
from sympy import sympify, evalf

def calculate(expression, decimals):
    # ChatGPT helped me a lot with this one because
    # I suck at math and I am very unfamiliar with these
    # libraries but I still tried my best to understand this
    
    
    safe_math = {
    'sqrt': math.sqrt,
    'sin': math.sin,
    'cos': math.cos,
    'log': math.log,
    'exp': math.exp,
    'pow': pow,
    'pi': math.pi,
    }
    
    try:
        expression = expression.replace('^', '**')
        
        expr = sympify(expression)
        
        return round(expr.evalf(subs=safe_math), decimals)
    except Exception as e:
        return e