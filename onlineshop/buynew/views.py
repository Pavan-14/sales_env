from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == "POST":
        # print('gotPOST')
        form = request.POST
        a = int(form.get("integer_A",None))
        b = int(form.get("integer_B",None))
        action = form.get("operation",None)
        result_val = 0

        if action == "add":
            result_val = a+b
        elif action == 'sub':
            result_val = a-b
        """
        else:
            print('select any one of the operator')
        """
        context = {"res":result_val}
        # print(context)
    else:
        # print('gotPOST')
        context = {}
    return render(request,"home.html",context)
