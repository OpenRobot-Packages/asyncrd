import asyncio, typing
import aioconsole
from .parser import Parser
from redis_protocol import decode, encode

class RedisOK():
    def __init__(self, message : str):
        self.msg = message
        
class BaseRedisException(Exception):
    pass

class RedisException(BaseRedisException):
    def __init__(self, message : str):
        super().__init__(message)
        
class RedisCommandUnknown(BaseRedisException):
    def __init__(self, message : str):
        super().__init__(message)
        
class RedisWrongType(BaseRedisException):
    def __init__(self, message : str):
        super().__init__(message)


class CatchException():
    def __init__(self, text : str):
        self.text = text
        
    async def catch_error(self):
        parser = Parser()
        decoded = await parser.decode(self.text)
            
        
