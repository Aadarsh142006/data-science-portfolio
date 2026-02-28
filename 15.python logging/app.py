import logging
## absic logging setting
logging.basicConfig(
level=logging.DEBUG,
format='%(asctime)s-%(name)s-%(message)s',
datefmt="%y-%m-%d %H:%M:%S",
force=True,
handlers=[
    logging.FileHandler('app1.log'),
    logging.StreamHandler()
]
)
logger=logging.getLogger("arthimetic app")

def add(a,b):
    result=a+b
    logger.debug(f"adding {a} +{b}={result}")
    return result
def sub(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def mul(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result
def div(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero attempted!")
        return None
add(2,3)
sub(14,3)
mul(20,1)
div(12,2)