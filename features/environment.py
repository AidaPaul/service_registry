from multiprocessing import Process
from Registry import *
from RESTService import *
    
def before_all(context):
    context.service = Process(target=RESTService.start)
    context.service.start()
    
    registry = Registry()
    registry.reset()


def after_all(context):
    context.service.terminate()
