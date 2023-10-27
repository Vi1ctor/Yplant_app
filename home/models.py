# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Classification(models.Model):
    nitrogen = models.FloatField()
    potassium = models.FloatField()
    calcium = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_ph = models.FloatField()
    ground_precipitation = models.FloatField()
    available_water_annual = models.FloatField()
    classification = models.TextField()
    forecast_date = models.DateField(default=timezone.now)
    usuario = models.ForeignKey(
        to=CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
    )

    def __str__(self):
        return (
            f"Classification [\n"
            f"  nitrogen={self.nitrogen},\n"
            f"  potassium={self.potassium},\n"
            f"  calcium={self.calcium},\n"
            f"  temperature={self.temperature},\n"
            f"  humidity={self.humidity},\n"
            f"  soil_ph={self.soil_ph},\n"
            f"  ground_precipitation={self.ground_precipitation},\n"
            f"  available_water_annual={self.available_water_annual},\n"
            f"  classification={self.classification}\n""]"
        )


  