import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from academy.serializers import User
from my_calendar.models import Event
from django.utils import timezone


@pytest.mark.django_db
def test_event_list_grouped_by_status():
    client = APIClient()
    user = User.objects.create_user(username="user1", password="pass")
    client.force_authenticate(user=user)

    # Создаем события с разными статусами
    event_upcoming = Event.objects.create(
        event_type="training",
        start_time=timezone.now() + timezone.timedelta(days=1)
    )
    event_invited = Event.objects.create(
        event_type="meeting",
        start_time=timezone.now() + timezone.timedelta(hours=2)
    )
    event_invited.participants.add(user)

    url = reverse("event-list")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert "upcoming" in response.data
    assert "invited" in response.data
    assert "all" in response.data


@pytest.mark.django_db
def test_event_create():
    client = APIClient()
    user = User.objects.create_user(username="user2", password="pass")
    client.force_authenticate(user=user)

    url = reverse("event-list")
    data = {
        "event_type": "game",
        "description": "Test Game Event",
        "start_time": timezone.now() + timezone.timedelta(hours=1),
        "end_time": timezone.now() + timezone.timedelta(hours=2),
        "reminder_enabled": True,
        "reminder_time": 15  # За 15 минут до события
    }
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["event_type"] == "game"
    assert response.data["reminder_enabled"] is True
    assert response.data["reminder_time"] == 15
