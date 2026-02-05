#!/usr/bin/env python3
from abc import ABC, abstractmethod

class IPrecioProvider(ABC):
    
    @abstractmethod
    def get_precio():
        pass

