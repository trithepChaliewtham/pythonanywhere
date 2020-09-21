from django.db import models


#
#
#
class Fruit(models.Model):

    # Fruit_ID = models.IntegerField(pirmary_key=True)
    Fruit_ID = models.IntegerField()
    Fruit_Name = models.CharField(max_length=200)


    def __str__(self):

        return f'{self.Fruit_ID}'

class Fruit_Type(models.Model):

    FruitID = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    Fruit_Price = models.CharField(max_length=200)
    Season_of_Fruit = models.CharField(max_length=200)

    def __str__(self):

        return f'{self.Fruit_Price} , {self.Season_of_Fruit}'
