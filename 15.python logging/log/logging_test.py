### configure logging
import logging
logging.basicConfig(
filename='app.log',
filemode='w',
level=logging.DEBUG,
format='%(asctime)s-%(name)s-%(message)s',
datefmt="%y-%m-%d %H:%M:%S",
force=True

)