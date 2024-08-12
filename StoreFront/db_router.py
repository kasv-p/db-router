from .context_manager import *


class DBReadWriteRouter:

    def db_for_read(self, model, **hints):
        if not get_is_default_db_request():
            return get_db_for_request()
        return None

    def db_for_write(self, model, **hints):
        if not get_is_default_db_request():
            return get_db_for_request()
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None

