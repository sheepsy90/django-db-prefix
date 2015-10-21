from django.conf import settings
from django.db.models.signals import pre_init


def add_db_prefix(sender, **kwargs):
    prefix = getattr(settings, "DB_PREFIX", None)
    if isinstance(prefix, dict):
        app_label = sender._meta.app_label.lower()
        sender_name = sender._meta.object_name.lower()
        full_name = app_label + "." + sender_name
        if full_name in prefix:
            prefix = prefix[full_name]
        elif app_label in prefix:
            prefix = prefix[app_label]
        else:
            prefix = prefix.get(None, None)
    if prefix:
        sender._meta.db_table = prefix + sender._meta.db_table


pre_init.connect(add_db_prefix)
