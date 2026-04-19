import logging

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not args:
            args = 'none'
        if not kwargs:
            kwargs = 'none'
        logger = logging.getLogger(func.__name__ + "_parameter_log")
        logger.setLevel(logging.INFO)
        logger.addHandler(logging.FileHandler("./decorator.log","a"))

        logger.log(logging.INFO, f"function: {func.__name__}\npositional parameters: {args}\nkeyword parameters: {kwargs}\nreturn: {result}\n")
        
        return result
    return wrapper



@logger_decorator
def hello():
    return f'Hello World'

@logger_decorator
def foo1(*args):
    return True
@logger_decorator
def foo2(*kwargs):
    return logger_decorator

hello()
foo1(5, 'red', True)
foo2(rust=True, python=True, java=False)