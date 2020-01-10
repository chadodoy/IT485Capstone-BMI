# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views import generic

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import logout
from accounts.models import BmiInfo
from newsletter.models import Subscription, Newsletter, Submission
from django.contrib.auth.decorators import login_required


def login_and_signup(request):

	# POST request (only when already on this for)
    if request.method == 'POST':

        print("test post ------------")

    	# Login user
        if 'loginuser' in request.POST and 'loginpass' in request.POST:
                print("loginuser", request.POST["loginuser"])
                user = authenticate(username= request.POST['loginuser'], password=request.POST['loginpass'])
                login(request, user)
                return redirect('home')

        # Sign up user
        else:
            form = UserCreationForm(request.POST)
            print(dir(form))

	        # Check that form fields are filled out and valid
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                height = float(request.POST['height'])
                weight = float(request.POST['weight'])
                bmi = int(100 * (weight/(height ** 2) * 703)) / 100
                print("BMI INFO ---------", bmi)
                if (bmi > 25):
                    bmi_status = str("overweight")
                elif(bmi > 17 and bmi < 25):
                    bmi_status = str("healthy")
                else:
                    bmi_status = str("underweight")
                user = authenticate(username=username, password=raw_password)
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.email = form.cleaned_data.get('username')
                user.save()
                BmiInfo.objects.create(user=user, height=float(height), weight=float(weight), bmi_info=bmi, bmi_stat=bmi_status)
                if "subscribe" in request.POST:
                    print("subscribe -----------", request.POST["subscribe"])
                    if request.POST['subscribe'] == "on":
                        newsletter_obj = Newsletter.objects.get(title="Henry")

                        Subscription.objects.create(user=user, email=str(user), name=str(user), newsletter=newsletter_obj, subscribed=True)

                login(request, user)
                return redirect('home')
            else:
                print(form.errors)
    else:
        print("test not post ----------------")
        form = UserCreationForm()
        print(dir(form.fields))
        print(dir(Subscription))
    return render(request, 'registration/login.html', {'form': form})

# def logout_view(request):
    logout(request)


@login_required
def home(request):
    bmi = BmiInfo.objects.get(user=request.user)
    return render(request, 'home.html', {'bmi_info': bmi})


def bmiform(request):
    if request.user.is_authenticated:
        update_db = ""
    else:
        update_db = "None"
    if request.method == "POST":
        print("POST SENT")
        height = float(request.POST['height'])
        weight = float(request.POST['weight'])
        bmi = int(100 * (weight/(height ** 2) * 703)) / 100
        if (bmi > 25):
            bmi_status = str("overweight")
        elif(bmi > 17 and bmi < 25):
            bmi_status = str("healthy")
        else:
            bmi_status = str("underweight")
        bmi_obj = BmiInfo.objects.get(user=request.user)
        bmi_obj.height = height
        bmi_obj.weight = weight
        bmi_obj.bmi_info = bmi
        bmi_obj.bmi_stat = bmi_status
        bmi_obj.save()
        return render(request, 'bmiform.html', {'updated_text' : "", "update_db": update_db})
    else:
        return render(request, 'bmiform.html', {'updated_text' : "None", "update_db": update_db})
# def bmi_form(request):
# 	return render(request, 'bmi_form.html' {})


# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'


#def index(request):
    #if request.method == "POST":
        #if request.POST.get('submit') == 'sign_in':
            # your sign in logic goes here
    	 #b elif request.POST.get('submit') == 'sign_up':
            # your sign up logic goes here
