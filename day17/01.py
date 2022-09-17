from pyparsing import nestedExpr
import json
a = '[[[[[9,8],1],2],3],4]'

exp = json.loads(a)
print(exp)


def process_exp(expr):
    while True:
        check_explosion(expr)

def check_explosion(expr, depth=0, left=None, right=None):
    left = expr[0]
    right = expr[0]
    if isinstance(left, list):
        check_explosion(expr=left, depth=depth)
    if isinstance(right, list):
        check_explosion(expr=right, depth=depth)


if __name__ == '__main__':
    process_exp(exp)