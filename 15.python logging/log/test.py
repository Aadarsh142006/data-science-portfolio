import logging
### configure logging
logging.basicConfig(
    filename='app.log',
    filemode='w',
level=logging.DEBUG,
format='%(asctime)s-%(name)s-%(message)s',
datefmt="%y-%m-%d %H:%M:%S",
force=True
)
def add(a,b):
    logging.debug("done additon called")
    return a+b
logging.debug("addition done")
add(2,4)