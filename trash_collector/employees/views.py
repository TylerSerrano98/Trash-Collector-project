from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from datetime import date
from .models import Employee

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.

@login_required
def index(request):
    logged_in_user = request.user
    try:
        logged_in_employee = Employee.objects.get(user = logged_in_user)
        today = date.today()
        logged_in_employee_zipcode = logged_in_employee.zip_code
        Customer = apps.get_model('customers.Customer')
        todays_customers = Customer.objects.filter(zip_code = logged_in_employee_zipcode)
        context = {
            'todays_customers': todays_customers
        }
        return render(request, 'employees/index.html')
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('employees:create'))


def determine_day():
    





    return










def confirm_pickup(request, customer_id):
    return







def view_schedule(request, weekday):
    return






@login_required
def create(request):
    return




@login_required
def edit_profile(request):
    return