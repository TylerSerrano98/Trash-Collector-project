from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.contrib.auth.decorators import login_required

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.

@login_required
def index(request):
    logged_in_user = request.user
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')



def determine_day():










def confirm_pickup(request, customer_id):







def view_schedule(request, weekday):






@login_required
def create(request):




@login_required
def edit_profile(request):