from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignupPageView


# Create your tests here.
class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="Urchman", email="iernest61@gmail.com", password="Abcdefgh_1"
        )
        self.assertEqual(user.username, "Urchman")
        self.assertEqual(user.email, "iernest61@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin", email="superadmin@email.com", password="Abcdefgh_1"
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpPageTests(TestCase):
    """
    Test suite for the sign-up page of the Django web application.

    Methods:
        - setUp:
          Set up preconditions for each test method by retrieving the URL for the sign-up page
          and performing a GET request.

        - test_signup_template:
          Test whether the sign-up page returns a 200 status code, uses the expected template
          ("registration/signup.html"), contains the text "Sign Up," and does not contain
          the text "Hi there! I should not be on the page."

    Usage:
        Run these tests to verify the correct functioning of the sign-up page views and templates.
    """

    def setUp(self):
        """
        Set up preconditions for each test method.

        This method is called before each test method to set up any necessary preconditions.
        In this case, it retrieves the URL for the sign-up page and performs a GET request,
        storing the response in the instance variable self.response for use in the test methods.
        """
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        """
        Test whether the sign-up page returns a 200 status code, uses the expected template
        ("registration/signup.html"), contains the text "Sign Up," and does not contain
        the text "Hi there! I should not be on the page."
        """
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_signup_form(self):
        """
        Test whether the sign-up form in the sign-up page context is an instance of
        the CustomUserCreationForm and contains the CSRF token.
        """
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        """
        Test whether the URL "/accounts/signup/" resolves to the expected SignupPageView.
        """
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
