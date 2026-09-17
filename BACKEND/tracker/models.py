from django.db import models

class AttackLog(models.Model):
    ip_address = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    threat_level = models.CharField(max_length=50, default='Unknown')
    attack_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.threat_level}"
