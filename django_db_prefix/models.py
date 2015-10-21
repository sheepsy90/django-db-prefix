from django.conf import settings
from django.db.models.signals import pre_init


def add_db_prefix(sender, **kwargs):
    prefix = getattr(settings, "DB_PREFIX", None)
    if prefix and not sender._meta.db_table.startswith(prefix):
        sender._meta.db_table = prefix + sender._meta.db_table


pre_init.connect(add_db_prefix)
