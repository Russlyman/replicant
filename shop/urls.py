from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="home"),
    path("item/<int:product_id>", views.product, name="product"),
]