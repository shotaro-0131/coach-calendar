from django.db import models

# Create your models here.

class User(models.Model):
    """コーチ"""
    familyName = models.CharField('苗字', max_length=100)
    firstName = models.CharField('名前', max_length=100)
    isRower = models.BooleanField('漕手', default=True)
    def __str__(self):
        return self.familyName + self.firstName

class Plan(models.Model):
    """予定"""
    people = models.ForeignKey(User, verbose_name='コーチ', related_name='plans', on_delete=models.CASCADE)
    year = models.IntegerField('年')
    month = models.IntegerField('月')
    day = models.IntegerField('日')
    isRow = models.BooleanField('乗艇日', default=False)
