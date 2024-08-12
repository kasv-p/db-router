from contextvars import ContextVar

db_for_request = ContextVar("db_name_for_request")
is_default_db_for_request = ContextVar("is_default_db")


def set_db_for_request(db):
    return db_for_request.set(db)


def get_db_for_request():
    try:
        return db_for_request.get()
    except:
        print("returning None...")
        return None


def set_is_default_db_request(is_default_db):
    return is_default_db_for_request.set(is_default_db)


def get_is_default_db_request():
    try:
        return is_default_db_for_request.get()
    except:
        print("returning None...")
        return None


def clear_context(default_db_token=None, token=None):
    if token:
        try:
            db_for_request.reset(token)
        except LookupError:
            print("this is not expected...")
            pass
    if default_db_token:
        try:
            is_default_db_for_request.reset(default_db_token)
        except LookupError:
            print("this is not expected...")
            pass
