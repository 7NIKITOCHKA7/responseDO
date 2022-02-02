from django.urls import path

from . import views

urlpatterns = [
    path('204', views.response204),
    path('200', views.response200),
    path('500', views.response500),
    path('exc', views.response204_exc),
    path('exc_no_custom',views.response204_exc_no_custom),
    path('exc2', views.response204_exc2)
]