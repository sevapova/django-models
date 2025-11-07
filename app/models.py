from django.db import models


class Task(models.Model):
    PRIOTRY_CHOICES = [
        ['1', 'Muxum'],
        ['2', 'Sal Muxum'],
        ['3', 'qilmasa ham boladi'],
        ['4', 'asosiy'],
    ]
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True, default="")
    priority = models.CharField(
        choices=PRIOTRY_CHOICES,
        default='4'
    )

    def __repr__(self):
        return f'Task(id={self.id}, name="{self.name}")'

    def __str__(self):
        return f'Task(id={self.id}, name="{self.name}")'


class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, default='', blank=True)
    age = models.PositiveSmallIntegerField()
    tg_id = models.BigIntegerField()

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f'user(id={self.id}, name="{self.full_name}")'
    