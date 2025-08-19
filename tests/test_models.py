import pytest
from django.utils import timezone
from my_calendar.models import Event, RepeatOption
from accounts.models import User
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_event_creation():
    creator = User.objects.create(username="test_user", password="test_password")
    event = Event.objects.create(
        creator=creator,
        event_type="training",
        description="Training event",
        start_time=timezone.now() + timezone.timedelta(hours=1),
        end_time=timezone.now() + timezone.timedelta(hours=2),
        reminder_enabled=True,
        reminder_time=10  # За 10 минут до события
    )

    assert event.event_type == "training"
    assert event.description == "Training event"
    assert event.reminder_enabled is True
    assert event.reminder_time == 10


@pytest.mark.django_db
def test_repeat_option_creation():
    repeat_option = RepeatOption.objects.create(repeat_option="every_monday")
    assert repeat_option.repeat_option == "every_monday"


@pytest.mark.django_db
def test_get_reminder_time():
    User = get_user_model()
    creator = User.objects.create_user(username='testuser', password='testpass')

    event = Event.objects.create(
        creator=creator,
        event_type="game",
        start_time=timezone.now() + timezone.timedelta(hours=1),
        reminder_time=10
    )
