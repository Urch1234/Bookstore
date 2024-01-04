from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView


class HomePageTests(SimpleTestCase):
    """
    Test suite for the home page (root URL) of the Django web application.
    """

    def setUp(self):
        """
        Set up preconditions for each test method.

        This method is called before each test method to set up any necessary preconditions.
        In this case, it retrieves the URL for the "home" page and performs a GET request,
        storing the response in the instance variable self.response for use in the test methods.
        """
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        """
        Test whether the root URL ("/") exists and returns a 200 status code.
        """
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_templates(self):
        """
        Test whether the correct template ("home.html") is used for rendering the home page.
        """
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        """
        Test whether the home page ("/") contains the expected HTML content.
        """
        self.assertContains(self.response, "home page")

    def test_homepage_does_not_contain_incorrect_html(self):
        """
        Test whether the home page ("/") does not contain specific incorrect HTML content.
        """
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_homepageview(self):
        """
        Test whether the URL "/" resolves to the expected HomePageView.

        This test uses the Django `resolve` function to find the view function
        associated with the root URL ("/"). It then compares the resolved view's
        function name with the expected function name of the `HomePageView` class-based view.
        """
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
