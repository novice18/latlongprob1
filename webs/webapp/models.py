from django.db import models

class landslideprob(models.Model):
    id=models.IntegerField(primary_key=True)
    prob=models.DecimalField(max_digits=10, decimal_places=5)
    lat=models.DecimalField(max_digits=20, decimal_places=7)
    #lon=models.DecimalField(max_digits=20, decimal_places=7)

    def __str__(self):
        return '{} : {}'.format(self.id, self.prob)
