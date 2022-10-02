from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == "POST":
        form = request.POST
        a = int(form.get("integer_A",None))
        b = int(form.get("integer_B",None))
        action = form.get("operation",None)
        result = 0

        if action == "add":
            result = a+b
        elif action == 'sub':
            result = a-b
        else:
            print('select any one of the operator')
        context = {"res":result}
        print(context)
    else:
        print('gotGET')
        context = {}

    return render(request,"home.html",context)