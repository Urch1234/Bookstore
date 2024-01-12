from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class CustomUserTest(TestCase):
    """
    Test case for custom user model functionality.

    Methods:
    - test_create_user: Test the creation of a regular user.
    - test_create_superuser: Test the creation of a superuser.
    """

    def test_create_user(self):
        """
        Test creating a regular user and verify user attributes.
        """
        User = get_user_model()
        user = User.objects.create_user(
            username="Urchman", email="iernest61@gmail.com", password="Abcdefgh_1"
        )
        self.assertEqual(
            user.username, "Urchman", msg="Username mismatch for regular user"
        )
        self.assertEqual(user.email, "iernest61@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """
        Test creating a superuser and verify superuser attributes.
        """
        user = get_user_model()
        admin_user = user.objects.create_superuser(
            username="superadmin", email="superadmin@email.com", password="Abcdefgh_1"
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpPageTests(TestCase):
    """
    Test case for the signup page functionality.

    Attributes:
    - username: A sample username for testing.
    - email: A sample email address for testing.

    Methods:
    - setUp: Set up the initial conditions for testing.
    - test_signup_template: Test the rendering of the signup template.
    - test_signup_form: Test the signup form submission and user creation.
    """

    username = "newuser"
    email = "newuser@email.com"

    def setUp(self):
        """
        Set up the initial conditions for testing the signup page.
        """
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        """
        Test the rendering of the signup template.
        """
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_signup_form(self):
        """
        Test the signup form submission and user creation.
        """
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
