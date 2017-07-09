import logging
import traceback
import inspect

#==================================================#
# Short example of how to create a simple but effective logging class in python.
# Docs: https://docs.python.org/2/howto/logging.html
# Cookbook: https://docs.python.org/2/howto/logging-cookbook.html
#==================================================#
class _Logger():
    def __init__(self,name):
        # Name the logger
        self.logger = logging.getLogger(name)

        # Set Log level
        self.logger.setLevel(logging.DEBUG)

        # Create file handler which logs all messages
        fh = logging.FileHandler('lol.log')
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

        # Create formatter and add it to the handlers
        # Print date and time prescending every log
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def trace(self,funcName):
        callerframerecord = inspect.stack()[1]    # 0 represents this line, 1 represents line at caller
        frame = callerframerecord[0]
        info = inspect.getframeinfo(frame)
        line = info.lineno
        err  = traceback.print_exc()
        Logging.error( "Function :: %s >> Error at Line: %s:\n{%s\n}"%(funcName,line,err) )


# HOW TO USE

if __name__ == "__main__":
    LOG = _Logger("logging_howto.py").logger

    # Create some logs from lowest to highest level
    LOG.debug("Houston, we have a %s", "thorny problem", exc_info=1)
    LOG.info('info')
    LOG.warning('warning')
    LOG.error('error')
    LOG.critical('critical')
    LOG.exception("exception")