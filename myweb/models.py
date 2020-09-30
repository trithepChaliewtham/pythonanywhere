from django.db import models


#
#
#
class Fruit(models.Model):
    summer = 1
    rainning = 2
    winter = 3
    allseason = 4
    season_choices = (
        (summer, 'ฤดูร้อน'),
        (rainning, 'ฤดูฝน'),
        (winter, 'ฤดูหนาว'),
        (allseason, 'ทุกฤดู'),
    )
    FrName = models.CharField(max_length=200,default="Banana")
    Season_Fruit = models.PositiveSmallIntegerField(choices=season_choices, default=summer)
    Price = models.FloatField(default=0)
    def __str__(self):
        
        return f'{self.FrName}';


class Farm(models.Model):
    name = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return f'{self.name}'

class Link(models.Model):
    Fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    Farm = models.ForeignKey(Farm, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Fruit} - {self.Farm}'