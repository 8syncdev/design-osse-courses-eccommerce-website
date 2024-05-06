from django.db import connections



def table_exists_util(table_name):
    return table_name in connections['default'].introspection.table_names()