from django.shortcuts import render,redirect
from .models import Myskill , Contactpage
from django.contrib.auth import authenticate,login,logout

def home(request):
    item = Myskill.objects.all()
    title = "Welcome To MDARIF"
    desc = "Web design refers to the design of websites that are displayed on the internet."
    context = {
        'title':title, 
        'description':desc,
        'data': item,
    }
    
    return render(request, 'index.html',context)

def about(request):
    title ="About Page for Skill Apps"
    desc = """Web design refers to the design of websites that are displayed on the internet. It usually refers to the user experience aspects of website development rather than software development. Web design used to be focused on designing websites for desktop browsers; however, since the mid-2010s, design for mobile and tablet browsers has become ever-increasingly important."""
    context = {
        'title': title,
        'Description': desc,
    }
    return render (request, 'about.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        querry = request.POST.get('comments')

        #mydata = Contactpage(name = name, email = email, querry = querry)
        mydata = Contactpage()

        mydata.cname = name
        mydata.cemail = email
        mydata.cquerry = querry

        mydata.save()
        
    return render(request, 'contact.html')

def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username, password= password)
        if user is not None:
            login(request, user)
            return redirect("home")
            #print("username:" +username)
        else:
            print("user not found")
            return render(request, "login.html")


def SignUp(request):
    logout(request)
    return redirect('login')
    