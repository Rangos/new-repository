from django_filters import FilterSet
from .models import Loans

class LoansFilter(FilterSet):
    class Meta:
        model = Loans
        fields = {"customer_station": ["exact"], "loan_status": ["exact"],
                  "loan_date":["gte"], "due_date":["lte"]}
