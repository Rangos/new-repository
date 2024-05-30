from django_tables2 import SingleTableView
from django.shortcuts import render
#from django.views.generic import ListView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.views.decorators.cache import cache_page
from django.views import generic
from django.views.generic import View 
from rest_framework.views import APIView
from rest_framework .response import Response
from django.db.models import Sum
from django.http import JsonResponse
from .models import Loans, Unit_Station_Names
from .tables import LoansTable
from .filters import LoansFilter


# Create your views here.
########################################### NEW TABLE BASED VIEWS
#@cache_page(60 * 15)
#loans list view
#@cache_page(600)
class LoanListView(SingleTableView):
    model = Loans
    table_class = LoansTable
    paginate_by = 15
    template_name = 'core/loanlist.html'
    
class LoanDetailView(generic.DetailView):
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
    paginate_by = 50
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
    
########################################### CHART VIEWS
## if you don't want to use rest_framework return response json
#loans chart view
def home(request):
    return render(request, 'home.html')

def loans_chart(request):
    labels =[]
    data = []

    queryset = Loans.objects.values('customer_station').annotate(loan_amount=Sum('loan_amount'))
    for entry in queryset:
        labels.append(entry['customer_station'])
        data.append(entry['loan_amount'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

## if you want to use rest_framework
## using rest_framework classes
class unit_station2(View): 
	def get(self, request, *args, **kwargs): 
		return render(request, 'core/unit_station_chart2.html') 

class unit_station_chart2(APIView):
    authentication_classes =[]
    permission_classi=es =[]

    def get(self, request, format =None):
        labels =[]
        data = []
        queryset = Unit_Station_Names.objects.all()
        
        for entry in queryset:
            #chartLabel = "my data"
            labels.append(entry.unit_station_name)
            data.append(entry.monthly_target)

        
        return Response(data={ 'labels':labels,
                'data':data,
            })
