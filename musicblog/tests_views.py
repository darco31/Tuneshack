from django.test import TestCase


class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_get_post_page(self):
        response = self.client.get('add_comment')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_comment.html')

    # def add_post_page(self):

    # def delete_post_page(self):

    # def add_comment_page(self):

    # def edit_post_page(self):
