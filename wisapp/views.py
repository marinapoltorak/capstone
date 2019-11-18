from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Scientist
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html',{ 'form':form })

def index(request):
    scientists = Scientist.objects.all().order_by('name')
    context = {
        'scientists': scientists,
    }
    return render(request, 'wisapp/index.html', context)

# @login_required
# def save_scientist(request):
#     print(request.POST)
#     user = request.user
#     sci_image = request.POST['sci_image']
#     sci_name = request.POST['sci_name']
#     sci_bio = request.POST['sci_bio']
#
#     scientist = Scientist(user=user, sci_image=sci_image, sci_name=sci_name, sci_bio=sci_bio)
#     scientist.save()
#
#     return HttpResponseRedirect(reverse('wisapp:index'))

@login_required
def get_a_scientist(request):
    db_scientists = Scientist.objects.order_by('sci_name')
    scientists = []
    for db_scientist in db_scientists:
        image = db_scientist.sci_image.url
        bio = db_scientist.sci_bio
        name = db_scientist.sci_name
        big_stuff = db_scientist.sci_big_stuff
        sci_field = db_scientist.sci_field
        scientists.append({
            'image': image,
            'bio': bio,
            'name': name,
            'big_stuff': big_stuff,
            'sci_field' : sci_field,
        })

    return JsonResponse({'scientists': scientists})

@login_required
def save_a_scientist_ajax(request):
    data = json.loads(request.body)
    image = data['image']
    bio = data['bio']
    name = ['name']
    big_stuff = ['big_stuff']
    sci_field = ['sci_field']
    user = request.user

    scientist = Scientist(user=user, image=image, sci_name=sci_name, sci_bio=sci_bi, )
    scientist.save()

    return HttpResponse('ok')
