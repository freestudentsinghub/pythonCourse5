from django.db import models

from config.settings import AUTH_USER_MODEL


class Habits(models.Model):
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец привычки", blank=True,
                              null=True)
    location = models.CharField(max_length=200, default="Дома", verbose_name="Место выполнения привычки")
    habit_time = models.DateTimeField(verbose_name="Дата и время выполнения привычки")
    action = models.CharField(max_length=200, verbose_name="Выполняемое действие")
    nice_habit = models.BooleanField(default=False, verbose_name="Приятная привычка", blank=True, null=True)
    associated_habit = models.ForeignKey("self", on_delete=models.SET_NULL, verbose_name="Связанная привычка",
                                         blank=True, null=True)
    period = models.PositiveIntegerField(verbose_name="Период выполнения привычки", blank=True, null=True)
    award = models.CharField(max_length=200, verbose_name="Вознаграждение", blank=True, null=True)
    complete_time = models.DurationField(verbose_name="Время на выполнение привычки", blank=True, null=True)
    is_public = models.BooleanField(default=True, verbose_name="Публичность привычки", blank=True, null=True)

    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"