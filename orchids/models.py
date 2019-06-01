from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

WEATHER_ANDES = 'ANDES'
WEATHER_COAST = 'COAST'
STATE_NOT_ASSIGNED = 'NOT_ASSIGNED'
STATE_ASSIGNED = 'ASSIGNED'
STATE_SOLD = 'SOLD'
STATE_DESTROYED = 'DESTROYED'
VARS_DAY = 'VARS_DAY'

CHOICES_WEATHERS = (
    (WEATHER_ANDES, WEATHER_ANDES),
    (WEATHER_COAST, WEATHER_COAST),
)


class Vars(models.Model):
    name = models.CharField(max_length=10, default='', unique=True)
    value = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5000)])

    @classmethod
    def create(cls, name, value):
        entity = cls(name=name, value=value)

        return entity


class Greenhouse(models.Model):
    name = models.CharField(max_length=6, default='', unique=True)
    weather = models.CharField(max_length=10, default='', choices=CHOICES_WEATHERS)
    temperature = models.IntegerField(default=15, validators=[MinValueValidator(5), MaxValueValidator(25)])
    capacity = models.IntegerField(default=1000, validators=[MinValueValidator(100), MaxValueValidator(2000)])
    available = models.IntegerField(default=0)

    @classmethod
    def create(cls, name, weather, temperature, capacity):
        entity = cls(name=name, weather=weather, temperature=temperature, capacity=capacity, available=capacity)

        return entity


class Orchid(models.Model):
    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=6, default='', unique=True)
    preferred_weather = models.CharField(max_length=10, default='', choices=CHOICES_WEATHERS)
    number = models.IntegerField(default=100, validators=[MinValueValidator(1), MaxValueValidator(300)])
    min_temperature = models.IntegerField(default=10, validators=[MinValueValidator(5), MaxValueValidator(25)])
    max_temperature = models.IntegerField(default=20, validators=[MinValueValidator(5), MaxValueValidator(25)])
    original_days_in_andes = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(20)])
    original_days_in_coast = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(20)])
    current_days_in_andes = models.IntegerField(default=5)
    current_days_in_coast = models.IntegerField(default=5)
    state = models.CharField(max_length=20, default=STATE_NOT_ASSIGNED)

    @classmethod
    def create(cls, name, preferred_weather, number, min_temperature, max_temperature, original_days_in_andes,
               original_days_in_coast):
        entity = cls(name=name, preferred_weather=preferred_weather, number=number, min_temperature=min_temperature,
                     max_temperature=max_temperature, original_days_in_andes=original_days_in_andes,
                     original_days_in_coast=original_days_in_coast, current_days_in_andes=original_days_in_andes,
                     current_days_in_coast=original_days_in_coast)

        return entity
