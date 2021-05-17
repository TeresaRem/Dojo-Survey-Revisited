from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method == "POST":
        ninja_name = request.POST['ninja_name']
        location = request.POST['location']
        languages = request.POST['languages']
        comments = request.POST['comments']
        request.session['ninja_name'] = ninja_name
        request.session['location'] = location
        request.session['languages'] = languages
        request.session['comments'] =  comments
        #context = {
        #    "ninja_name": ninja_name,
        #    "location" : location,
        #    "languages" : languages,
        #    "comments" : comments
        # }
    #return render(request,'show.html',context)
    return redirect('/show')

def show(request):
    print(request.session)
    print('got here to show from redirect')
    return render(request,'show.html')