from django.test import TestCase
from django.urls import reverse

class  HomePageTests(TestCase):
    def test_page_home_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_home_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home page')
    def test_home_page_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_home_page_template_use(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

