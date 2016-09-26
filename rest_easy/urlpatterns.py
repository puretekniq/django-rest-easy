from rest_easy import decorators


def pop_rest_urlpatterns(urlpatterns):
    urlpatterns.extend(decorators._urlpatterns)
    decorators._urlpatterns = []