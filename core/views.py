from django.shortcuts import render, HttpResponse


html_base = """
<h1> mi web </h1>
<ul>
<li><a href = "/" >home</a></li>
<li><a href = "/about" >Acerca de </a></li>
<li><a href = "/services" >services  </a></li>
<li><a href = "/store" >store </a></li>
<li><a href = "/contact" >Contact  </a></li>
<li><a href = "/blog" >blog  </a></li>
<li><a href = "/sample" >sample  </a></li>

</ul>
"""
# Create your views here.

def home(request):
    return render(request, "core/home.html") 

def about(request):
     return render(request, "core/about.html") 
  
# def services(request):
#     return render(request, "core/services.html")

def store(request):
    return render(request, "core/store.html") 

  


    
    
"""def home(request):
    return HttpResponse(html_base+"<h1> mi web </h1><p>jhsgajsgdjahsd </p>")
def about(request):
    return HttpResponse(html_base+"<h1> Historia </h1><h2>Acerca de: </h2> <p>productos electronicos para gamers</p>")
def services(request):
    return HttpResponse(html_base+"<h1> Servicios </h1><h2>Acerca de: </h2> <p>empresa fundada en el 2018</p>")
def store(request):
    return HttpResponse(html_base+"<h1> Visitanos </h1><h2>Acerca de: </h2> <p>empresa fundada en el 2018</p>")
def contact(request):
    return HttpResponse(html_base+"<h1> Contacto </h1><h2>Acerca de: </h2> <p>empresa fundada en el 2018</p>")
def blog(request):
    return HttpResponse(html_base+"<h1> Blog </h1><h2>Acerca de: </h2> <p>empresa fundada en el 2018</p>")
def sample(request):
    return HttpResponse(html_base+"<h1> Sample </h1><h2>Acerca de: </h2> <p>empresa fundada en el 2018</p>")"""