from functools import wraps

from StoreFront.context_manager import set_db_for_request, clear_context


def using_db(db_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = set_db_for_request(db_name)
            try:
                result = func(*args, **kwargs)
            finally:
                clear_context(token=token)
            return result

        return wrapper

    return decorator
