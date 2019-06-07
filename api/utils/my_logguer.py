import logging

class MyFilter:
    def __init__(self,level):
        self.level=level
    def filter(self, logRecord):
        return logRecord.levelno ==self.level

# logger=logging.getLogger('')
# logger.setLevel(logging.DEBUG)
handler1= logging.FileHandler('./info.log','w')
handler1.setLevel(logging.INFO)
handler1.addFilter(MyFilter(logging.INFO))
formater=logging.Formatter("%(levelname)s- %(message)s")
handler1.setFormatter(formater)
# logger.addHandler(handler1)
# logging._addHandlerRef(handler1)
handler=logging.StreamHandler()
handler.setLevel(logging.WARNING)
formater=logging.Formatter("%(levelname)s- %(message)s")
handler.setFormatter(formater)
handler.addFilter(MyFilter(logging.WARNING))
# logger.addHandler(handler)
# logging._addHandlerRef(handler)
logging.basicConfig(level=logging.DEBUG,handlers=[handler1,handler])
