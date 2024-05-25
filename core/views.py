from django_tables2 import SingleTableView
from django.shortcuts import render
#from django.views.generic import ListView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.views import generic
from .models import Loans
from .tables import LoansTable
from .filters import LoansFilter


# Create your views here.
########################################### NEW TABLE BASED VIEWS
#loans list view
class LoanListView(SingleTableView):
    model = Loans
    table_class = LoansTable
    paginate_by = 15
    template_name = 'core/loanlist.html'
    
class LoanDetailView(SingleTableMixin, generic.DetailView):
    model = Loans
    table_class = LoansTable

    template_name = 'core/loandetail.html'

    
#filter data in tables
class FilteredLoansListView(SingleTableMixin, FilterView):
    table_class = LoansTable
    model = Loans
    template_name = "core/loanfilter.html"

    filterset_class = LoansFilter


########################################### NEW CLASS BASED VIEWS
class LoansListView1(generic.ListView, FilterView):
    model = Loans
    context_object_name = 'loan_list'
    template_name = "core/new.html"
    #paginate_by = 10
    filterset_class = LoansFilter
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(LoansListView1, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class LoansDetailView1(generic.DetailView):
    model = Loans
    template_name = "core/new1.html"
    
