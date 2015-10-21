django_db_prefix
================

Project goal
------------

Allow specification of a global, per-app or per-model database table
name prefix.

Reason for the project
----------------------

1. Some (external) projects automatically use a database prefix for 
   interaction with a database. This is particularly common in implementations
   of the Active Record pattern.

2. It is possible to define an explicit database table name in the Meta
   class on a model; however, this is not as easily accomplished when dealing
   with a third-party application. By providing a high-level interface for
   adding prefixes there is a simple, consistent way to achieve this goal other
   than forking the code or ad-hoc monkey patching.

Installation
------------

1. Install using pip:

    pip install git+https://github.com/maxvyaznikov/django-db-prefix.git

2. Add django_db_prefix at the top of your INSTALLED_APPS list. It is
   recommended that django_db_prefix is the first listed application, but it
   is essential that it be loaded before the initialization of any model you
   expect to be modified.

Configuration
-------------

Three configuration options are allowed: global, per-app or per-model. In all
cases, the specified prefix will be prepended exactly as provided -- no
delimiter will be added.

In all cases, behavior is controlled by the `DB_PREFIX` setting.

Global Prefix
=============

To add a common prefix to all models simply set `DB_PREFIX` to the string that
you want to be prepended.

    DB_PREFIX = "foo_"

For example, for the model bar_app.models.Baz the default table would be:
`bar_app_baz`

By setting `DB_PREFIX` to `foo_`, the table would be `foo_bar_app_baz`.
