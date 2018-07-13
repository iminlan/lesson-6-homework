from django.urls import path
from catalog.views import detail

urlpatterns = [
    path('<int:id>', detail, name='market-catalog-detail')
]
