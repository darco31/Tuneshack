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

    def test_contact_page(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_thanks_page(self):
        response = self.client.get('/thanks')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thanks.html')

    def test_add_comment_page(self):
        response = self.client.get('/article/35/add_comment')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_comment.html')

