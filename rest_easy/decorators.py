
from django.conf.urls import url as add_url

# accumulation of URL patterns, will be 'popped' and put into module's urlpatterns
_urlpatterns = []


def rest_url(url_regex, methods=None, name=None):
    def url_decorator(original_function):
        _name = name
        if not _name:
            _name = original_function.__name__
        # print("url_decorator " + repr(original_function) + " " + url_regex + " " + _name)
        _urlpatterns.append(add_url(url_regex, original_function, None, _name, None))

        def new_function(*args, **kwargs):
            return original_function(*args, **kwargs)

        return new_function

    return url_decorator
