from django.db import models


class PhoneTracking(models.Model):
    imei = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.imei}"
