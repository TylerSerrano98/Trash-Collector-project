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
        todays_customers = Customer.objects.filter(zipcode = logged_in_employee_zipcode)
        context = {
            'todays_customers': todays_customers
        }
        return render(request, 'employees/index.html')
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('employees:create'))


def determine_day():
    pass










def confirm_pickup(request, customer_id):
    pass







def view_schedule(request, weekday):
    pass






@login_required
def create(request):
    logged_in_user = request.user
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        address_from_from= request.POST.get('address')
        zip_from_from= request.POST.get('address')
        new_employee = Employee(name=name_from_form, user=logged_in_user, address=address_from_from, zip_code=zip_from_from)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')


@login_required
def edit_profile(request):
    pass