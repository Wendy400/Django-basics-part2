from django.shortcuts import render, redirect, get_object_or_404
from sokoapp.models import*

# Create your views here.

def error(request) :
    return render(request, '404.html')

def details(request) :
    return render(request, 'blog-details.html')

def blog(request) :
    return render(request, 'blog.html')

def index(request) :
    if request.method == 'POST':
        mycontact = Contact(
            name = request.POST ['name'],
            email =request.POST['email'],
            subject =request.POST['subject'],
            message =request.POST['message'],
        
        )
        mycontact.save()
        return redirect('/')
    else:
        return render(request, 'index.html')




def portfolio(request) :
    return render(request, 'portfolio-details.html')

def service(request) :
    return render(request, 'service-details.html')

def starter(request) :
    return render(request, 'starter-page.html')

def show(request) :
    all = Contact.objects.all()
    return render(request, 'show.html', {"all" : all})

def delete(request, id):
    contactinfo = Contact.objects.get(id=id)
    contactinfo.delete()
    return redirect('/show')

def edit(request, id):
    editcontact = get_object_or_404(Contact, id=id)

    if request.method == "POST":
        editcontact.name = request.POST.get('name')
        editcontact.email = request.POST.get('email')
        editcontact.subject = request.POST.get('subject')
        editcontact.message = request.POST.get('message')

        editcontact.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html')
    

        

