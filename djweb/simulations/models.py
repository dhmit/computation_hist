from django.db import models


class Simulation(models.Model):
    name = models.CharField(max_length=191, blank=True)

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return f"<{self.name}>"
