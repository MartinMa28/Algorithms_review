def greeting(name: str):
    def inner_func():
        print('Hello ' + name + '!')

    return inner_func

def add(a):
    return lambda b: lambda c: a + b + c

if __name__ == "__main__":
    greeter = greeting('Yilin')

    greeter()

    print(add(1)(10)(100))