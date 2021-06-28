from django.db import models

# Create your models here.
class MonthlyDataUpload(models.Model):
    id = models.AutoField(primary_key = True)
    upload_datetime = models.DateTimeField(auto_now_add=True)
    beneficiaries_assisted_males = models.IntegerField()
    beneficiaries_assisted_females = models.IntegerField()
    cash_value = models.IntegerField()
    country_iso3 = models.CharField(max_length=3)