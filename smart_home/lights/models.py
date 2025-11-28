from django.db import models

class Light(models.Model):
    light_id = models.CharField(max_length=10, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.light_id})"

    class Meta:
        app_label = 'lights'
