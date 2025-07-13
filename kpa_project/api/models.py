# forms/models.py
from django.db import models

# Main WheelSpecification form model
class WheelSpecification(models.Model):
    formNumber = models.CharField(max_length=100, unique=True)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()
    status = models.CharField(max_length=50, default="Saved")  # default status

    def __str__(self):
        return self.formNumber

# Related nested fields model
class WheelSpecificationFields(models.Model):
    spec = models.OneToOneField(WheelSpecification, on_delete=models.CASCADE, related_name='fields')

    # All fields inside the `fields` JSON structure
    treadDiameterNew = models.CharField(max_length=100)
    lastShopIssueSize = models.CharField(max_length=100)
    condemningDia = models.CharField(max_length=100)
    wheelGauge = models.CharField(max_length=100)
    variationSameAxle = models.CharField(max_length=100)
    variationSameBogie = models.CharField(max_length=100)
    variationSameCoach = models.CharField(max_length=100)
    wheelProfile = models.CharField(max_length=100)
    intermediateWWP = models.CharField(max_length=100)
    bearingSeatDiameter = models.CharField(max_length=100)
    rollerBearingOuterDia = models.CharField(max_length=100)
    rollerBearingBoreDia = models.CharField(max_length=100)
    rollerBearingWidth = models.CharField(max_length=100)
    axleBoxHousingBoreDia = models.CharField(max_length=100)
    wheelDiscWidth = models.CharField(max_length=100)
 

