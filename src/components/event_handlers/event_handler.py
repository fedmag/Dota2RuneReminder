import abc

class EventHandlerInterface(abc.ABC):
    
    @abc.abstractmethod
    def handle_state(self, state) -> None:
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_handler_name(self) -> str:
        raise NotImplementedError
    
    
