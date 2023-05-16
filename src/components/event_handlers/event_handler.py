import abc

class EventHandlerInterface(abc.ABC):
    
    @abc.abstractmethod
    def handle_event(self, event) -> None:
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_handler_name(self) -> str:
        raise NotImplementedError
    
    
