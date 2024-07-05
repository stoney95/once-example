import functools
import logging

logger = logging.getLogger(__name__)

def debug_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f"Calling {func.__name__}")
        
        result = func(*args, **kwargs)
        logger.debug(f"Finished calling {func.__name__}. Result: {result}")
        return result
    
    setattr(wrapper, '__once_decorated__', True)
    return wrapper

def log_exception(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Exception in {func.__name__}: {e}")
    
    return wrapper