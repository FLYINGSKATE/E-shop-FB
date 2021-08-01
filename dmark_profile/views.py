from django.shortcuts import render,HttpResponse, redirect,HttpResponseRedirect
from .models.employee import Employee
from django.views import View
from .models.contact import Contact_details

def index(request):
    return render(request, 'html/index.html')

def service(request):
    return  render(request, 'html/services.html')

class Career(View):
    def get(self, request):
        return render(request, 'html/career.html')

    def post(self, request):
        postData = request.POST
        hiring = postData.get('hiring')
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        phone_number = postData.get('phone_number')
        email_id = postData.get('email_id')
        description = postData.get('description')
        error_message = None
        value = {'fn':first_name,
                 'ln':last_name,
                 'pn':phone_number,
                 'email':email_id,
                 'des':description}
        employees = Employee(applied_for = hiring,
                             first_name_taken=first_name,
                             last_name_taken = last_name,
                             phone_number_taken = phone_number,
                             email_id_taken = email_id,
                             description_taken = description
                             )
        print(hiring,first_name, last_name , phone_number, email_id, description)
        error_message = self.validation(employees)
        if not error_message:

            employees.save_this()
            messages_reply = 'Your Request Has Been Sended'
            # return HttpResponseRedirect('career',messages_reply)
            return render(request, 'html/career.html',{'mass':messages_reply})

        else:
            data = {
                'value':value,
                'error':error_message
            }
            return render(request, 'html/career.html',data)


    def validation(self,employees):
        error_message = None
        if (not employees.applied_for):
            error_message = 'Select your Job !!'
        elif (not employees.first_name_taken):
            error_message = 'Enter your First Name !!'
        elif len(employees.first_name_taken) < 4:
            error_message = 'Name is too short !!'
        elif (not employees.last_name_taken):
            error_message = 'Enter your Surname or Last Name !!'
        elif len(employees.last_name_taken) < 4:
            error_message = 'surname or Last Name is too short !!'
        elif (not employees.phone_number_taken):
            error_message = 'Phone Number must required !!'
        elif len(employees.phone_number_taken) < 10:
            error_message = 'Enter the correct Phone Number !!'
        elif (not employees.email_id_taken):
            error_message = 'Email ID must required !!'
        return error_message

def about(request):
    return  render(request, 'html/about.html')

class Contact_us(View):
    def get(self, request):
        return  render(request, 'html/contact.html')
    def post(self, request):
        postData = request.POST
        name = postData.get('name')
        phone_number = postData.get('phone_number')
        email = postData.get('email')
        subject = postData.get('subject')
        message = postData.get('message')
        error_message = None
        value = {
            'n':name,
            'pn':phone_number,
            'e':email,
            'sub':subject,
            'mess':message
        }
        customer = Contact_details(name=name,
                                   phone_no = phone_number,
                                   email = email,
                                   subject = subject,
                                   message = message)
        error_message = self.validation(customer)
        print(name, phone_number, email,subject,message)
        if not error_message:
            customer.save_this_also()
            message_of = 'Your Message has been sended.'
            return render(request, 'html/contact.html',{'mess':message_of})
        else:
            data = {
                'value':value,
                'error':error_message
            }
            return render(request, 'html/contact.html',data)

    def validation(self, customer):
        error_message = None
        if (not customer.name):
            error_message = 'Enter Your Name !!'
        elif len(customer.name) < 4:
            error_message = 'Your Name is too Short !!'
        elif len(customer.phone_no) < 10:
            error_message = 'Enter Valid Phone Number !!'
        elif (not customer.email):
            error_message = 'Enter your Email ID So that we can connect with you'
        elif (not customer.message):
            error_message = 'Enter Your Message !!'
        return error_message

def private_policy(request):
    return  render(request, 'html/privacy.html')