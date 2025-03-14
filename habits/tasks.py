from datetime import datetime, timedelta

import pytz
from celery import shared_task
from django.conf import settings
from django.utils import timezone

from habits.models import Habits
from habits.services import send_telegram_message


@shared_task()
def telegram_message():

    timezone.activate(pytz.timezone(settings.CELERY_TIMEZONE))
    zone = pytz.timezone(settings.CELERY_TIMEZONE)
    now = datetime.now(zone)
    habits = Habits.objects.all()

    for habit in habits:
        user_tg = habit.user.tg_chat_id
        if (
            user_tg
            and now >= habit.habit_time - timedelta(minutes=10)
            and now.date() == habit.habit_time.date()
        ):
            if habit.is_nice:
                message = f"Ты получил {habit.action} в {habit.habit_time+timedelta(hours=3)} {habit.location}"
            else:
                message = f"Напоминание: {habit.action} в {habit.habit_time+timedelta(hours=3)} {habit.location}"

            send_telegram_message(user_tg, message)

            if habit.award:
                send_telegram_message(user_tg, f"Поздравляю! Ты получил: {habit.award}")

            habit.habit_time += timedelta(days=habit.period)
            habit.save()