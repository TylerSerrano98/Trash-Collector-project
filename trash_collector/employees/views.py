from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from datetime import date
from .models import Employee
from datetime import datetime

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.

@login_required
def index(request):
    logged_in_user = request.user
    try:
        today = datetime.now
        logged_in_employee = Employee.objects.get(user = logged_in_user)
        today = date.today()
        logged_in_employee_zipcode = logged_in_employee.zip_code
        Customer = apps.get_model('customers.Customer')
        todays_customers = Customer.objects.filter(zip_code = logged_in_employee_zipcode)
        context = {
            'todays_customers': todays_customers,
            'date': today,
            'logged_in_employee': logged_in_employee
        }
        return render(request, 'employees/index.html', context)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('employees:create'))


def determine_day(request):
    today = datetime.now
    context = {
            'date': today
        }
    return render(request, 'employees/index.html', context)
   
    
    
def charge_customer(request):
    if buttonclick:
       Customer.balance + 20

 





def confirm_pickup(request):
    Customer = apps.get_model('customers.Customer')
    logged_in_user = request.user

    logged_in_employee = Employee.objects.get(user=logged_in_user)
    employee_zip_code = logged_in_employee.zip_code

    if request.method == "POST":
        weekday_from_form = request.POST.get('days')

        customer_match = Customer.objects.filter(zip_code=employee_zip_code)\
            .filter(weekly_pickup = weekday_from_form)\

        selected_day = weekday_from_form

        context = {
            'customer_match': customer_match,
            'logged_in_employee': logged_in_employee,
            'selected_day': selected_day
        }

        return render(request, 'employees/confirm_pickup.html', context)
    else:
        today = date.today()

        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        today_weekday = days[today.weekday()]

        customer_match = Customer.objects.filter(zip_code=employee_zip_code)\
            .filter(weekly_pickup=today_weekday)

        selected_day = today_weekday

        context = {
            'customer_match': customer_match,
            'logged_in_employee': logged_in_employee,
            'selected_day': selected_day 
        }
        return render(request, 'employees/weekday_pickup_search.html', context)







def view_schedule(request, weekday):
    pass






@login_required
def create(request):
    logged_in_user = request.user
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        address_from_from= request.POST.get('address')
        zip_from_from= request.POST.get('zip_code')
        new_employee = Employee(name=name_from_form, user=logged_in_user, address=address_from_from, zip_code=zip_from_from)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')




@login_required
def edit_profile(request):
    logged_in_user = request.user
    logged_in_user = Employee.objects.get(user=logged_in_user)
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        address_from_form = request.POST.get('address')
        zip_from_form = request.POST.get('zip_code')
        logged_in_user.name = name_from_form
        logged_in_user.address = address_from_form
        logged_in_user.zip_code = zip_from_form
        logged_in_user.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        context = {
            'logged_in_employee': logged_in_user
        }
        return render(request, 'employees/edit_profile.html', context)