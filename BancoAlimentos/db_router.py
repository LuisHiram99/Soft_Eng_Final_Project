class AccidentesRouter:
    """
    A router to control all database operations on models in the
    accidentes application.
    """
    def db_for_read(self, model, **hints):
        """Point all operations on accidentes models to 'accidentes'."""
        if model._meta.app_label == 'main':
            return 'accidentes'
        return None

    def db_for_write(self, model, **hints):
        """Point all operations on accidentes models to 'accidentes'."""
        if model._meta.app_label == 'main':
            return 'accidentes'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation if a model in the accidentes app is involved."""
        if obj1._meta.app_label == 'main' or obj2._meta.app_label == 'main':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Make sure the accidentes app only appears in the 'accidentes' database."""
        if app_label == 'main':
            return db == 'accidentes'
        return None


