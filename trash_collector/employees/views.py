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
    Customer = apps.get_model('customers.Customer')
    logged_in_user = request.user
    if request.method == "POST":
       today = date.today()
       id_from_form = request.POST.get('id')
       
       complete_customer = Customer.objects.get(id=id_from_form)
       complete_customer.date_of_last_pickup = today

       complete_customer.balance += 20
       complete_customer.save()

       return HttpResponseRedirect(reverse('employees:index'))
    
    try:
        logged_in_employee = Employee.objects.get(user = logged_in_user)
        logged_in_employee_zipcode = logged_in_employee.zip_code
        today = date.today()

        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        today_weekday = days[today.weekday()]

        todays_customers = Customer.objects.filter(zip_code = logged_in_employee_zipcode)\
            .filter(weekly_pickup=today_weekday)\
            .exclude(date_of_last_pickup=today)\
            .exclude(suspend_start=today)\
            .exclude(suspend_end=today)\
            .exclude(one_time_pickup=today)
        
        context = {
            'logged_in_employee': logged_in_employee,
            'today': today,
            'today_weekday': today_weekday,
            'todays_customers': todays_customers,
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
        return render(request, 'employees/confirm_pickup.html', context)

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