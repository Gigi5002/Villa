from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseTest(TestCase):
    def setUp(self):
        # Создайте тестового пользователя
        self.test_user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        # Вы можете создать другие общие настройки здесь
        # Например, тестовые объекты, используемые в других тестах
