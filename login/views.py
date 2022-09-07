from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.template import loader
from . import serializers
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import login as auth_login, authenticate
from django.views.decorators.csrf import csrf_protect
from login.forms import RegisterForm
import requests
from django.contrib.sessions.models import Session

# Create your views here.
class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer

    def create(self, request):
        print("new request")
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            password = request.data.get("password")  # plain password
            user = serializer.save()
            user.set_password(password)  # encrypt password
            user.save()

            return Response(status=200, data={"msg": "User has been registered."})
        else:
            return Response(status=500, data={"msg": "Unable to register user."})

    # def list(self, request):
    #     return Response(status=403,data={"msg": "API not allowed."})

    def retrieve(self, request, pk=None):
        return Response(status=403, data={"msg": "API not allowed."})

    def update(self, request, pk=None):
        return Response(status=403, data={"msg": "API not allowed."})

    def partial_update(self, request, pk=None):
        return Response(status=403, data={"msg": "API not allowed."})

    def destroy(self, request, pk=None):
        return Response(status=403, data={"msg": "API not allowed."})

@csrf_protect
def register(request):
    if request.method == 'POST':
        signup = RegisterForm(request.POST)
        if signup.is_valid():
            response = requests.post('http://localhost:8000/api/v1/register/', request.POST)
            print('response', response.text)
            if response.status_code == 200:
                username = signup.cleaned_data.get('username')
                raw_password = signup.cleaned_data.get('password')
                print(username)
                print(raw_password)
                user = authenticate(username=username, password=raw_password)
                if user is not None:
                   auth_login(request, user)
                   return redirect('/')
                else:
                    return HttpResponse("Problem while registering.")

    csrfContext = RequestContext(request)
    signup_form = RegisterForm() # dictionary
    return render(request,'register.html',{'form': signup_form},csrfContext) # passed to object as form


class LoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.LoginSerializer

    def create(self, request):
        print("new request")
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                authenticate.login(request, user)
                return redirect("/")
            else:
                return Response(status=404,data={"success": False})
        except Exception as e:
            print(e)
            return Response(status=501,data={"msg": "Problem while logging in user."})

    def list(self, request):
        return Response(status=403,data={"msg": "API not allowed."})

    def retrieve(self, request, pk=None):
        return Response(status=403,data={"msg": "API not allowed."})

    def update(self, request, pk=None):
        return Response(status=403,data={"msg": "API not allowed."})

    def partial_update(self, request, pk=None):
        return Response(status=403,data={"msg": "API not allowed."})

    def destroy(self, request, pk=None):
        return Response(status=403,data={"msg": "API not allowed."})


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        # count = User.objects.filter(username=username, password=password).count()
        # if count >0:
        #     request.sessions['is_logged'] = True
        #     return redirect('home')
        # else:
        #     messages.error(request,'Incorrect username and password')
        #     return redirect('login')
        # user = auth.authenticate(username=username,password= password)

    #     if user is not None:
    #         auth.login(request, user)
    #         return redirect("/")
    #     else:
    #         messages.info(request,'invalid credentials')
    #         return redirect('login')
    # else:
    #      return render(request,'login.html')

