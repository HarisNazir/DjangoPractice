from rest_framework import serializers

from .models import MonthlyDataUpload

class MonthlyDataUploadSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MonthlyDataUpload
        fields = ('id', 'upload_datetime', 'beneficiaries_assisted_males', 'beneficiaries_assisted_females', 'cash_value','country_iso3')