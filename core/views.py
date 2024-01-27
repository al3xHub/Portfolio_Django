from django.shortcuts import render, HttpResponse
html_base = """
<ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about-me/">About me</a></li>
    <li><a href="/portfolio/">Portfolio</a></li>
    <li><a href="/contact/">Contact</a></li>
</ul>
"""
# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about-me.html")

def contact(request):
    return render(request, "core/contact-us.html")
