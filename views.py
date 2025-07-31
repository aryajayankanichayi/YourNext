from django.shortcuts import render,redirect
from .models import *
from .movies import *
# Create your views here.
genre_map = fetch_genre_map()
print(genre_map)

def index(request):
    return render(request,"index.html")

def login(request):
    msg=""
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists()==True:
            user=User.objects.get(email=email)
            if user.check_password(password) == True:
                request.session["uid"] = user.id
                return redirect("/userhome")
            else:
                msg="Password Incorrect"
        else:
            msg="Email is not registered"
    return render(request,"login.html",{"msg":msg})

def registration(request):
    msg=""
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        languages = request.POST['languages']
        selected_genres = request.POST.getlist('genre')
        genres = ""
        for i in selected_genres:
            genres+=i+","
        if User.objects.filter(email=email).exists() != True and User.objects.filter(username=username).exists() != True :
            user=User.objects.create_user(username=username,email=email,password=password,languages=languages,genres=genres)
            user.save()
            msg = "Registration Successfull"
        else:
            msg="Username or Email Already Exists"

        
    return render(request,"registration.html",{'msg':msg})

def userhome(request):
    msg = ""
    user = User.objects.get(id=request.session['uid'])
    if request.method == 'POST':
        query = request.POST.get('query', '').lower()
        if 'watch' in query.split():
            genres = ""
            for g in genre_map:
                if g in query:
                    genres += g + ','
            if genres == "":
                genres = user.genres
            genre_names = [g.strip().lower() for g in genres.strip(',').split(',') if g.strip()]
            genre_ids = [str(genre_map[g]) for g in genre_names if g in genre_map]

            if genre_ids:
                movies = get_movies(genre_ids, 'en')
                return render(request, "userhome.html", {
                    'msg': msg,
                    'user': user,
                    'movies': movies
                })
            else:
                msg = "No valid genres found."

    return render(request, "userhome.html", {
        'msg': msg,
        'user': user
    })


def profile(request):
    return render(request,"profile.html")

def watched(request):
    return render(request,"watched.html")

def favorite(request):
    return render(request,"favorite.html")

def about(request):
    return render(request,"about.html")