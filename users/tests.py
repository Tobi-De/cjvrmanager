from django.contrib.auth.models import User
from django.test import TestCase


class ProfileModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="tobi", password="**blumen**")

    def test_user_has_profile(self):
        self.assertTrue(self.user.profile, f"{self.user.username} Profile")


class SignupViewTests(TestCase):

    def test_signup(self):
        self.client.post('/signup/', {
            "username": "francis",
            "password1": "**blumen**",
            "password2": "**blumen**",
        })
        self.assertTrue(User.objects.filter(username="francis").exists())


"""class MySeleniumTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User.objects.create_user(username="tobi", password="**blumen**")
        cls.selenium = webdriver.Firefox(executable_path="/home/tobi/gecko/geckodriver")
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_Login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("tobi")
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("**blumen**")
        self.selenium.find_element_by_name("login").click()"""
