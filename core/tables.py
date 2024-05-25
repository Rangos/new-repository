import django_tables2 as tables
from .models import Loans, Loan_Status, Unit_Station_Names

class LoansTable(tables.Table):
   
    class Meta:
        model = Loans
        template_name = "django_tables2/bootstrap.html"
        fields = ("id","loan_date", "due_date", "loan_code", "loan_amount",
                 "customer_station", "customer_id", "loan_status" )
