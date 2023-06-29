from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import User
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    user_list = User.objects.order_by('-date_added')[:10]
    context = {'user_list': user_list}
    return render(request, 'userlist/index.html', context)

def add(request):
    return render(request, 'userlist/add.html')

def processadd(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    position = request.POST.get('position')
    if request.FILES.get('image'):
        user_pic = request.FILES.get('image')
    else:
        user_pic = 'profile_pic/image.jpg'
    try: 
        n = User.objects.get(user_email=email)
        # n already exists
        return render(request, 'userlist/add.html', { 'error_message' : "Email " + email + " already existed " })
    except ObjectDoesNotExist:
        user = User.objects.create(user_email=email, user_fname=fname, user_lname=lname, user_position=position, user_image=user_pic)
        user.save()
        return HttpResponseRedirect('/users')
    
def detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'userlist/detail.html', {'user': user})