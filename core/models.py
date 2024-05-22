from django.db import models

# Create your models here.
#loan status model
class Loan_Status(models.Model):
    loan_id = models.IntegerField(null=True, blank=True)
    loan_status = models.CharField(max_length=100)

    def __str__(self):
        return self.loan_status
        #return '{} : {}' .format (self.id, self.loan_status)
        
    

#unit station model
class Unit_Station_Names(models.Model):
    #station_id = models.IntegerField()
    unit_station_name = models.CharField(max_length=100)
    daily_target = models.IntegerField()
    monthly_target = models.IntegerField()

    def __str__(self):
        return self.unit_station_name
         #return '{} : {} : {} : {}' .format (self.id, self.unit_station_name, self.daily_target, self.monthly_target)
        
    
    
# loans model    
class Loans(models.Model):
    loan_date = models.DateField()
    due_date = models.DateField()
    loan_code = models.IntegerField()
    loan_amount = models.IntegerField()
    customer_station = models.ForeignKey(Unit_Station_Names, on_delete=models.CASCADE)
    customer_id = models.IntegerField()
    loan_status = models.ForeignKey(Loan_Status, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{} : {} : {}: {}: {}: {}: {} : {}' .format (self.id, self.loan_date, self.due_date, self.loan_code, self.loan_amount,
                self.customer_station, self.customer_id, self.loan_status)
    

