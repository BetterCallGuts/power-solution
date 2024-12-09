from django.shortcuts import render, redirect
from .models import Brand, Product,ProductImage
from django.views.generic import View



# 
def index(request):
    brands = Brand.objects.all().filter(deactivated=False)
    context = {
        'brands': brands,
        "home": "active",

        }
    return render(request, 'pages/home.html' , context=context)

# 
def UPS(request):

    context = {
        "UPS": "active",
        }
    return render(request, 'pages/store.html', context=context)


# 
def generator(request):
    context = {
        "generator": "active",
        }
    return render(request, 'pages/store.html', context=context)


# 

class Service(View):
    template_name = 'pages/services.html'
    def get(self, request):

        return render(request, 'pages/services.html')
# 
def detail(request, slug):
    print(slug)
    try: #{
        prod = Product.objects.get(slug=slug)
        print(prod)
        other= Product.objects.exclude(slug=slug).filter(category=prod.category)
        other_photos = ProductImage.objects.filter(product=prod)
    #}
    except: #{
        return redirect('index')
    #}
    context = {
        "product": prod,
        "other": other,
        "other_photos": other_photos,
    }
    return render(request, 'pages/Detail.html', context=context)

# 
def contact(req):

    return render(req, "pages/contact.html")

def accessories(req):
    UPSs = Product.objects.filter(category__name="UPS")
 
    context = {
        "accessories": "active",
        "UPSs": UPSs,
    }
    return render(req, "pages/accessories.html", context=context)