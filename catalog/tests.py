from django.test import TestCase
from django.urls import reverse

from catalog.data import BOOKS


class CatalogRouterTest(TestCase):
    def test_details(self):
        for book in BOOKS:
            response = self.client.get(reverse('market-catalog-detail', kwargs=dict(id=book['id'])))
            assert response.status_code == 200
            assert isinstance(response.context['book'], dict)
