# from django.test import TestCase, Client
# from django.urls import reverse
# from musicblog.models import Post, Comment


# class TestViews(TestCase):

#     def test_get_home_page(self):

#         client = Client()

#         response = client.get(reverse('/'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'home.html')

    # def test_get_post_page(self):
    #     response = self.client.get('/post-detail')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'post_detail.html')

    # def add_post_page(self):
    #     response = self.client.get('/add_post')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'add_post.html')

    # def delete_post_page(self):

    # def add_comment_page(self):

    # def edit_post_page(self):
