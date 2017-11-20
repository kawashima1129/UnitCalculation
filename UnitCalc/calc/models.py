from django.db import models

# Create your models here.
class Unit(models.Model):
    subject_name = models.CharField(max_length=200)
    subject_category = models.CharField(max_length=200)
    number_unit = models.IntegerField(default=2)

    def __str__(self):
        return self.subject_name

class Register_Unit(models.Model):
    Register_obj = models.ForeignKey(Unit)


class User(models.Model):
    compulsory_unit = models.IntegerField()
    select_unit = models.IntegerField()
    free_unit = models.IntegerField()
    core_unit = models.IntegerField()



