from .context_manager import *


class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        is_default_db = not request.path.startswith('/StoreFront/item')
        default_db_token = set_is_default_db_request(is_default_db)
        try:
            if not is_default_db:
                token = set_db_for_request("read_db" if request.method == "GET" else "write_db")
                response = self.get_response(request)
                clear_context(token=token)
            else:
                response = self.get_response(request)
        finally:
            clear_context(default_db_token=default_db_token)
        return response
