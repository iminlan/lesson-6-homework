from django.test import TestCase


class RouterTest(TestCase):
    def test_home(self):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_context(self):
        reponse = self.client.get('/')
        books = reponse.context['books']
        assert len(books) == 3
