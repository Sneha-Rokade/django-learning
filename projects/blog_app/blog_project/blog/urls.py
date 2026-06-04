from django.urls import path
from .views import home, post_detail

urlpatterns = [
    path('', home),
    path(
        'post/<int:id>/',
     post_detail
    ),
]