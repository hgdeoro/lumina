from lumina.settings import *  # noqa

DEBUG = False

#
# Dump object with {% dump_objects %}
#
LUMINA_DUMP_OBJECTS = False


try:
    import uwsgi
    from uwsgidecorators import timer
    from django.utils import autoreload

    @timer(3)
    def change_code_gracefull_reload(sig):
        if autoreload.code_changed():
            uwsgi.reload()

    print("AUTO-reloading of uWSGI activated")

except:
    import logging
    logging.exception("NOT using auto-reloading")
