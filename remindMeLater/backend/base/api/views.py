# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Reminder
from .serializers import ReminderSerializer
from django.utils import timezone

@api_view(['POST'])
def create_reminder(request):
    if request.method == 'POST':
        message = request.data.get('message')
        sendingDate = request.data.get('sendingDate')
        sendingTime = request.data.get('sendingTime')
        reminder_datetime = timezone.now()

        reminder = Reminder.objects.create(
            reminder_datetime=reminder_datetime,
            sendingDate=sendingDate,
            sendingTime=sendingTime,
            message=message
        )

        serializer = ReminderSerializer(reminder)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
