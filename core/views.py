from django_tables2 import SingleTableView
from django.shortcuts import render
from django.views.generic import ListView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .models import Loans
from .tables import LoansTable
from .filters import LoansFilter


# Create your views here.
#loans list view
class LoanListView(SingleTableView):
    model = Loans
    table_class = LoansTable
    template_name = 'core/loanlist.html'
    
#filter data in tables
class FilteredLoansListView(SingleTableMixin, FilterView):
    table_class = LoansTable
    model = Loans
    template_name = "core/loanfilter.html"

    filterset_class = LoansFilter
