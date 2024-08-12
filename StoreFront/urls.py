from django.urls import path
from . import views

urlpatterns = [
    path("item/<int:item_id>", views.get_item),
    path("item", views.add_item)
]
