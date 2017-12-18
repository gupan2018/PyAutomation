__author__ = 'Administrator'
import logging
logging.basicConfig(level=logging.DEBUG)

#-----------------------装饰器-----------------------------
    #我的理解是在函数开始执行和结束执行的时候自动执行的一段代码
    #————切面编程

def foo():
    print('i am foo')
    logging.info("foo is running")

def use_logging(func):
    def wrapper(*args, **kwargs):
        logging.warning("%s is running"%func.__name__)
        return func(*args, **kwargs)
    return wrapper

#-----------------------------------带参数的装饰器-------------------------
def use_logging_p(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warning("%s is running"%func.__name__)
            return func(*args, **kwargs)
        return wrapper

@use_logging
def bar():
    print("i am bar")

if __name__ == "__main__":
    #bar = use_logging(bar)
    bar()
    print("-------------------不用@装饰器语法糖----------------------")
    foo = use_logging(foo)
    foo()