from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
import ipfsApi
import sweetify

api = ipfsApi.Client('127.0.0.1', 5001)

# Create your views here.
def home(request):
	return render(request, 'dash/index.html')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			return redirect("register")
		else:
			for msg in form.error_messages:
				print(form.error_messages[msg])

	form = UserCreationForm
	return render(request, 'dash/register.html',context={"form":form})

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		print(username,password)
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request, user)
			print('Success')
			return render(request, 'dash/map.html')
	else:
			return render(request, 'dash/login.html')

def map(request):
	return render(request, 'dash/map.html')

def veh_info(request):
	return render(request, 'dash/tables.html')

def beh_analysis(request):
	return render(request, 'dash/beh_analy.html')

def drive(request):
	return render(request, 'dash/drive.html')
	# if request.method == 'POST':
	# 	file = request.POST['file']
		# print(file)
		# res = api.add(file)
		# if res:
		# 	print(res)
		#sweetify.success(request, 'IPFS HASH --> '+ res['Hash'] , text='Your file has been saved Successfully !!! :D',button='Ok', timer='10000')

	# else:
	

def profile(request):
	return render(request, 'dash/user.html')

def about(request):
	return render(request, 'dash/main_about.html')

def services(request):
	return render(request, 'dash/main_services.html')

def gallery(request):
	return render(request, 'dash/main_gallery.html')

def contact(request):
	return render(request, 'dash/main_contact.html')

def terms(request):
	return render(request, 'dash/main_terms.html')