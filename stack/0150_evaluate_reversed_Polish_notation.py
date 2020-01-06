def _validate_float(s_num) -> bool:
    s_num = s_num.strip()
    
    if s_num[0] == '+' or s_num[0] == '-':
        s_num = s_num[1:]

    if s_num.isdecimal():
        return True

    splitted = s_num.split('.')

    if len(splitted) != 2:
        return False
    elif splitted[0] and splitted[1]:
        return splitted[0].isdecimal() and splitted[1].isdecimal()
    elif splitted[0]:
        return splitted[0].isdecimal()
    elif splitted[1]:
        return splitted[1].isdecimal()
    else:
        return False

            
            
            




def eval_postfix(tokens):
    stack = []
    operators = {}
    
    operators['+'] = lambda a, b: a + b
    operators['-'] = lambda a, b: a - b
    operators['*'] = lambda a, b: a * b
    operators['/'] = lambda a, b: a / b

    for t in tokens:
        if t not in operators:
            if _validate_float(t):
                stack.append(float(t))
            else:
                raise Exception('Invalid input operands')
        else:
            try:
                right_op = stack.pop()
                left_op = stack.pop()

                evaluated = operators[t](left_op, right_op)
                stack.append(evaluated)
            except IndexError as err:
                raise Exception('Each binary operator must have 2 operands')
            except ZeroDivisionError as err:
                raise Exception('Cannot be divided by zero')
            except KeyError:
                raise Exception('Un-supported operator')
    
    if len(stack) > 1:
        raise Exception('Extra operands in the input!')
    else:
        return stack.pop()


if __name__ == "__main__":
    print(eval_postfix(['3.5', '3', '+', '2', '*', '3', '5', '/', '-', '10',
                        '+', '2', '-3.', '*', '-']))              