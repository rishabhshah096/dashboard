from django.db import models
import uuid

# Create your models here.
class Robots(models.Model):
    id = models.UUIDField( primary_key=True, default=uuid.uuid4,
                           help_text='Unique ID for this particular book across whole library' )
    name = models.CharField(max_length=100)
    waste_type = models.ForeignKey('Wasteitems',on_delete=models.SET_NULL,null=True)
    robot_type = models.CharField(max_length=100)

    def __str__(self):
        return '{}: - {}: - {}:'.format(self.name,self.waste_type,self.robot_type)

class Wasteitems(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    def __str__(self):
        return '{}'.format(self.name)