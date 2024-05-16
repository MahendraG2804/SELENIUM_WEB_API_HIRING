def factorial_func(num):
    assert num>=0 and type(num) is int, "Invalid input, Input must be positive integer"
    if num == 0 :
        return 1
    else :
        return num * factorial_func(num-1)
    
    