from typing import Callable, Optional

class Event:
    def __init__(self, listeners: Optional[list[Callable]] = None):
        self._listeners: list[Callable] = [] if listeners is None else listeners
        
    async def __iadd__(self, listener: Callable):
        self._listeners.append(listener)
        return self
    
    async def __call__(self, *args, **kwargs):
        for listener in self._listeners:
            listener(*args, **kwargs)