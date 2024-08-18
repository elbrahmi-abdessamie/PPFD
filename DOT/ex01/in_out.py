def square(x: int | float) -> int | float:
    return x ** 2

def pow(x: int | float)-> int | float:
    return x ** x

def outer(x: int | float, function) -> object:
    count = 0
    def inner()->float:
        nonlocal x, count
        count += 1
        x = function(x)
        return x
    return inner

def main():
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())

if __name__ == '__main__':
    main()