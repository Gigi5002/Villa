from django.test import TestCase
from unittest.mock import patch
from my_calendar.models import Event
from my_calendar.tasks import schedule_event_notification, send_event_notification
from django.utils import timezone
from datetime import timedelta


class NotificationTasksTestCase(TestCase):
    def setUp(self):
        # Создание тестового события
        self.event = Event.objects.create(
            creator=self.test_user,  # Укажите тестового пользователя
            event_type='Мероприятие',
            description='Спортивный день',
            start_time=timezone.now() + timedelta(minutes=30),
            reminder_time=15
        )
        # Добавьте участников, если необходимо

    @patch('my_calendar.tasks.send_event_notification')
    def test_schedule_event_notification(self, mock_send_event_notification):
        # Вызываем задачу планирования уведомления
        schedule_event_notification(self.event.id)

        # Проверяем, что send_event_notification была вызвана
        mock_send_event_notification.assert_called_once_with(self.event.id)

    @patch('my_calendar.tasks.messaging.send_multicast')
    def test_send_notification(self, mock_send_multicast):
        tokens = ['token1', 'token2']  # Пример токенов
        send_event_notification(self.event.id)  # Вызов функции отправки уведомлений

        # Проверка, что send_multicast была вызвана с правильными параметрами
        mock_send_multicast.assert_called_once()
        args, kwargs = mock_send_multicast.call_args[0]

        # Убедитесь, что сообщение содержит правильные данные
        self.assertEqual(kwargs['message']['notification']['title'], f"Напоминание: {self.event.event_type} начнется скоро!")
        self.assertEqual(kwargs['message']['data']['description'], self.event.description)
        self.assertEqual(kwargs['message']['tokens'], tokens)
