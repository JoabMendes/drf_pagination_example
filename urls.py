from django.conf.urls import url

from .views import ProductSearchAPIView


urlpatterns = [
    url(
        r'^product/?$',
        ProductSearchAPIView.as_view()
    ),
]

