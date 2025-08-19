from django.utils import timezone

from django.test import TestCase

from academy.serializers import User
from my_calendar.models import Event
from notification.models import UserDevicesID
from unittest.mock import patch
from my_calendar.tasks import send_event_notification, schedule_event_notification


class NotificationTaskTests(TestCase):
    @classmethod
    def setUpTestData(cls):        # Создание тестового пользователя
        cls.creator = User.objects.create(username="testuser", password="password", phone_number="1234567890")
        cls.user = User.objects.create(username="participant", password="password", phone_number="0987654321")

    @patch('your_app.tasks.send_notification')  # Замена на мок для функции отправки
    def test_send_event_notification(self, mock_send_notification):
        # Вызов задачи
        send_event_notification.apply((self.event.id,))

        # Проверка, что функция отправки была вызвана
        mock_send_notification.assert_called_once()
        # Проверка правильности переданных аргументов (токены и событие)
        self.assertEqual(mock_send_notification.call_args[0][0], ['test_device_token'])
        self.assertEqual(mock_send_notification.call_args[0][1], self.event)

    @patch('your_app.tasks.send_event_notification.delay')  # Замена на мок для задачи
    def test_schedule_event_notification(self, mock_send_event_notification):
        # Вызов задачи
        schedule_event_notification.apply((self.event.id,))

        # Проверка, что задача отправки уведомления была запланирована
        mock_send_event_notification.assert_called_once_with(self.event.id)

