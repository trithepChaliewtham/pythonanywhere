from django.db import models


#
#
#
class Fruit(models.Model):

    
    Fruit_ID = models.IntegerField(null=False)
    Fruit_Name = models.CharField(max_length=200)
    


    def __str__(self):

        return f'{self.Fruit_ID},{self.Fruit_Name}'
class Farm(models.Model):
    Farm_ID = models.IntegerField(null=False)
    Farm_Name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.Farm_ID},{self.Farm_Name}'

class Fruit_Type(models.Model):

    FruitID = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    Fruit_Names = models.CharField(max_length=200)
    Fruit_Price = models.CharField(max_length=200)
    Season_of_Fruit = models.CharField(max_length=200)
    FarmID = models.ForeignKey(Farm, on_delete=models.CASCADE)

    def __str__(self):

        return f'{self.Fruit_Name} ,{self.Fruit_Price} , {self.Season_of_Fruit}'
