from django.shortcuts import render, redirect
from .models import Brand, Product,ProductImage, RequestInfo, ProductHighLight, Ferbo
from django.views.generic import View
from django.contrib import messages
from django.db.models import Q


def contact_form_handler(request):
        name         = request.POST.get('name') 
        email        = request.POST.get('Email')
        phone_number = request.POST.get('phonenumber')
        company_name = request.POST.get('companyName')
        description  = request.POST.get('description')
        if name and email and phone_number and company_name :
            return [name , email, phone_number, company_name, description]
        else:
            messages.error(request, "Please fill all the fields")


# 
class index(View):
    def get(self, request):
            brands = Brand.objects.all().filter(deactivated=False)

            context = {
                'brands': brands,
                "home": "active"
                }
            
            return render(request, 'pages/home.html' , context=context)
    def post(self, request):
        li = contact_form_handler(request)
        if not li:
            return render(request, 'pages/home.html')


# 

class UPS(View):
    
    def get(self, request):
        context = {}
        upss = Product.objects.filter(category__name="UPS", page__name="ups")
        q    = request.GET.get('q')
        if q:
            upss = upss.filter(Q(name__icontains=q) | Q(description__icontains=q))
            context["q"] = q
            print(len(upss))
        context["UPSs"] = upss
        context["UPS"]  = "active"
        
        return render(request, 'pages/UPS.html', context=context)


class FerboDetailView(View):




    def get(self, req, slug):
        try:

            ferbo = Ferbo.objects.get(slug=slug)
        except:
            return redirect('index')

        context = {
            "generator": "active" ,
            "ferbo": ferbo        ,
            
        }
        return render(req, "pages/ferbo-detail.html", context=context)



class FerboView(View):

    def get(self, req):
        ferbos = Ferbo.objects.all()

        context = {
            "generator": "active",
            "ferbos": ferbos,

        }

        return render(req, "pages/ferbo.html", context=context)
# 
def generator(request):
    context = {
        "generator": "active",
        }
    return render(request, 'pages/store.html', context=context)


# 

class Service(View):
    
    def get(self, request,):
        return render(request, 'pages/services.html')
# 
class RequestInfoView(View):
    
    def get(self, request, slug):
        
        return render(request, 'pages/request-info.html')

    def post(self, request, slug):
        

        li = contact_form_handler(request)
        # 
        if not li:
            return render(request, 'pages/request-info.html')
        # 
        name , email, phone_number, company_name, description = li
        # 
        try:
            prod         = Product.objects.get(slug=slug)
            
        except:
            return redirect('index')
        # 
        req = RequestInfo.objects.create(
            name        = name,
            email       = email,
            phone       = phone_number,
            company     = company_name,
            description = description,
            prod        = prod,
            )
        req.save()
        messages.success(request, f"Your request has been sent successfully")
        return redirect('index')


class DetailView(View):


    def get(self,request, slug):
        
        try: #{
            prod = Product.objects.get(slug=slug)
            highlights   = ProductHighLight.objects.filter(product=prod)
            other_photos = ProductImage.objects.filter(product=prod)
            other= Product.objects.exclude(slug=slug).filter(category=prod.category, page=prod.page)
        #}
        except: #{
            return redirect('index')
        #}
        context = {
            "product": prod,
            "other": other,
            "other_photos": other_photos,
            "highlights" : highlights,
        }
        return render(request, 'pages/Detail.html', context=context)


class accessories_ups(View):
    
    def get(self, request):
            context = {}
            upss = Product.objects.filter(category__name="UPS", page__name="accessories")
            q    = request.GET.get('q')
            if q:
                upss = upss.filter(Q(name__icontains=q) | Q(description__icontains=q))
                context["q"] = q
                print(len(upss))
            context["UPSs"] = upss
            context["UPS"]  = "active"
            
            return render(request, 'pages/UPS.html', context=context)


class accessories_generator(View):
    def get(self, req,):
        pass