from datetime import timedelta

from rest_framework.serializers import ValidationError


class HabitValidators:
    """Валидатор проверяет все возможные требования технического задания."""

    def __call__(self, value):
        val = dict(value)  # конвертируем QuerySet в словарь
        if val.get("complete_time") > timedelta(seconds=120):
            raise ValidationError(
                "Внимание! Время выполнения привычки не может составлять больше 2-х минут !"
            )

        elif int(val.get("period")) < 1 or int(val.get("period")) > 7:
            raise ValidationError(
                "Внимание! Выполнять привычку нужно не реже чем 1 раз в 7 дней!"
            )

        elif (
            val.get("nice_habit") is False
            and not val.get("award")
            and not val.get("associated_habit")
        ):
            raise ValidationError(
                "Внимание! У полезной привычки необходимо заполнить одно из полей: "
                "'Вознаграждение' или 'Связанная привычка'! "
            )

        elif (
            val.get("nice_habit") is False
            and val.get("award")
            and val.get("associated_habit")
        ):
            raise ValidationError(
                "Внимание! У полезной привычки необходимо зполнить только одно из полей:"
                " 'Вознаграждение' или 'Связанная привычка'!"
            )

        elif val.get("nice_habit") is True and val.get("associated_habit"):
            raise ValidationError(
                "Внимание! У приятной привычки не может быть связанной привычки!"
            )

        elif val.get("nice_habit") is True and val.get("award"):
            raise ValidationError(
                "Внимание! У приятной привычки не может быть вознаграждения!"
            )