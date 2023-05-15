import abc

class EventHandlerInterface(abc.ABC):
    
    @abc.abstractmethod
    def handle_event(self, event):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_handler_name(self):
        raise NotImplementedError
    
    
