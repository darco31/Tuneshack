from django.test import TestCase
from musicblog.forms import PostForm, EditForm


class TestPostForm(TestCase):

    def test_title_field(self):
        form = PostForm({'title': 'Test title'})
        self.assertTrue(form.is_valid)

    def test_fields_explicit(self):
        form = EditForm()
        self.assertEqual(form.Meta.fields, ('title', 'body'))

    def test_fields_post(self):
        form = PostForm()
        self.assertEqual(form.Meta.fields, ('title', 'author', 'body'))
