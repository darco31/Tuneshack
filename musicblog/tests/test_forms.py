from django.test import TestCase
from musicblog.forms import PostForm, EditForm


class TestPostForm(TestCase):

    def test_item_name_required(self):
        form = EditForm({'body': ''})
        self.assertFalse(form.is_valid)

    def test_fields_explicit(self):
        form = PostForm()
        self.assertEqual(form.Meta.fields, ('title', 'author', 'body'))
