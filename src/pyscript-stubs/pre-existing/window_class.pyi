from .base import EventTarget

class Location:
    hostname: str

class Console:
    def log(self, output: any): ...

class FileReader(EventTarget):
    @classmethod
    def new(cls): ...

class Window(EventTarget):
    console: Console
    FileReader: FileReader
    location: Location