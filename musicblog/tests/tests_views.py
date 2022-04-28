from django.test import TestCase


class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_add_post_page(self):
        response = self.client.get('/add_post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_post.html')
