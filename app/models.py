from django.db import models

# Create your models here.

class MyUser(models.Model):
    class Meta:
        db_table = 'app_user'
    """コーチ"""
    familyName = models.CharField('familyname', max_length=100)
    firstName = models.CharField('firstname', max_length=100)
    isRower = models.BooleanField('漕手', default=True)
    user_id = models.IntegerField('user_id', max_length=100)
    def __str__(self):
        return self.familyName + self.firstName
    def create_user(self, familyName, firstName, userId):
        self.familyName = familyName
        self.firstName = firstName
        self.user_id = userId
        return self

class Plan(models.Model):
    """予定"""
    # people = models.ForeignKey(User, verbose_name='コーチ', related_name='plans', on_delete=models.CASCADE)
    menu = models.CharField('メニュー', max_length=100)
    year = models.IntegerField('年', default=0)
    month = models.IntegerField('月', default=0)
    day = models.IntegerField('日', default=0)
    isRow = models.BooleanField('乗艇日', default=False)

    def get_time(self):
        return int(str(year)+str(month)+str(day))
