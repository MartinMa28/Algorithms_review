def _only_digits(s_num):
    if not s_num:
        return False

    digits = set([str(n) for n in range(10)])

    for ch in s_num:
        if ch not in digits:
            return False
    return True

def _is_integer(s_num):
    if not s_num:
        return False
    else:
        if s_num[0] == '+' or s_num[0] == '-':
            s_num = s_num[1:]

        if s_num:
            return _only_digits(s_num) and s_num[0] != '0'
        else:
            return False

def _is_float(s_num) -> bool:
    if _is_integer(s_num):
        return True
    else:

        splitted_dot = s_num.split('.')
        if len(splitted_dot) != 2:
            return False
        else:
            return _is_integer(splitted_dot[0]) and _only_digits(splitted_dot[1])

            
class PostFixNotationError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        




def eval_postfix(tokens):
    stack = []
    operators = {}
    
    operators['+'] = lambda a, b: a + b
    operators['-'] = lambda a, b: a - b
    operators['*'] = lambda a, b: a * b
    operators['/'] = lambda a, b: a / b

    for t in tokens:
        if t not in operators:
            if _is_float(t):
                stack.append(float(t))
            else:
                raise PostFixNotationError('Invalid input operands')
        else:
            try:
                right_op = stack.pop()
                left_op = stack.pop()

                evaluated = operators[t](left_op, right_op)
                stack.append(evaluated)
            except IndexError as err:
                raise PostFixNotationError('Each binary operator must have 2 operands')
            except ZeroDivisionError as err:
                raise PostFixNotationError('Cannot be divided by zero')
            
    
    if len(stack) > 1:
        raise PostFixNotationError('Extra operands in the input!')
    else:
        return stack.pop()


if __name__ == "__main__":
    print(eval_postfix(['3.5', '3', '+', '2', '*', '3', '5', '/', '-', '10',
                        '+', '2', '-3.0', '*', '-']))              