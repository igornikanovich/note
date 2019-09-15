from django.test import TestCase
from django.urls import reverse

from NoteApp.models import Category, Note


class CategoryListViewTest(TestCase):
    def test_create_category_is_success(self):
        response = self.client.post(reverse('index'),
                                    {'name': 'testnamecat'})
        self.assertEqual(response.status_code, 302)


class AddTitleNoteViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test')
        self.category.save()

    def tearDown(self):
        self.category.delete()

    def test_get_response(self):
        response = self.client.get(reverse('Note-create', kwargs={'slug': self.category.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'noteapp/note_form.html')

    def test_create_title_to_note_is_success(self):
        response = self.client.post(reverse('Note-create', kwargs={'slug': self.category.slug}),
                                    {'title': 'testtitle'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 1)


class NoteTextUpdateViewTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test')
        self.note = Note.objects.create(title='testTitle', category=self.category)
        self.category.save()
        self.note.save()

    def tearDown(self):
        self.category.delete()
        self.note.delete()

    def test_get_response(self):
        response = self.client.get(reverse('Note-update', kwargs={'slug': self.note.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'noteapp/note_detail.html')

    def test_update_note_is_success(self):
        response = self.client.post(reverse('Note-update', kwargs={'slug': self.note.slug}),
                                    {'text': 'testtitle', 'password': 123456})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/Note/'))

    def test_update_is_fail_wrong_pass(self):
        response = self.client.post(reverse('Note-update', kwargs={'slug': self.note.slug}),
                                    {'text': 'testtitle', 'password': 111111})
        self.assertEqual(response.status_code, 200)
