from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse


def index(request):
    images = ProductImage.objects.all()[:10]
    categories = Category.objects.all()
    print(categories)
    brands = Brand.objects.all().order_by('name')
    if request.method == 'POST':
        print(request.POST)
        data = request.POST
        password = data['pw']
        username = data['us']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Успешно се најавивте.')
            return redirect('profile')
        else:
            messages.success(request, 'Невалидни податоци.')
            return render(request, 'index.html', context={'brands': brands, 'user': user})
    user = request.user
    return render(request, 'index.html',
                  context={'brands': brands, 'user': user, 'images': images, 'categories': categories})


def logout_view(request):
    if request.method == 'POST':
        brands = Brand.objects.all()
        logout(request)
        messages.success(request, 'Успешно се одјавивте.')
        user = request.user
        return render(request, 'index.html', context={'brands': brands, 'user': user})


def single_product(request, id):
    if request.method == 'POST':
        data = request.POST
        product = get_object_or_404(Product, id=id)
        product = str(product.name)
        email = data['email']
        message = data['message']
        try:
            send_mail(product, message, email, ['info@panatek.mk'], fail_silently=False, )
        except:
            pass
        product = get_object_or_404(Product, id=id)
        brands = Brand.objects.all()
        message_response = 'Ви благодариме за пораката. Нашите оператори ќе ве контактираат наскоро.'
        return render(request, 'single_product.html', context={'product': product, 'brands': brands, })
    else:
        categories = Category.objects.all()
        product = get_object_or_404(Product, id=id)
        brands = Brand.objects.all()
        return render(request, 'single_product.html',
                      context={'product': product, 'brands': brands, 'categories': categories})


def brands(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    return render(request, 'brands.html', context={'brands': brands, 'categories': categories})


def single_brand_view(request, name):
    categories = Category.objects.all()
    cats = Category.objects.filter(brand__name=name)
    brand = Brand.objects.get(name=name)
    brands = Brand.objects.all()
    products = Product.objects.filter(brand__name=name)
    return render(request, 'single_brand.html',
                  context={'cats': cats, 'brand': brand, 'brands': brands, 'products': products,
                           'categories': categories})


def catalogue(request, name):
    categories = Category.objects.all()
    products = Product.objects.filter(category__name=name)
    cat = Category.objects.get(name=name)
    brands = Brand.objects.all()
    return render(request, 'catalogue.html',
                  context={
                      'products': products,
                      'brand': cat.brand.name,
                      'name': cat,
                      'brands': brands,
                      'categories': categories
                  })


def profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user__id=request.user.id)
        products = profile.products.all()

        return render(request, 'profile.html', context={'user': user, 'profile': profile, 'products': products, })
    else:
        brands = Brand.objects.all()
        return render(request, 'index.html', context={'brands': brands})


def clients(request):
    if request.user.is_authenticated and request.user.is_superuser:
        user = request.user
        profile = Profile.objects.get(user__id=request.user.id)
        products = profile.products.all()
        profiles = Profile.objects.all()

        return render(request, 'clients.html',
                      context={'user': user, 'profile': profile, 'products': products, 'profiles': profiles, })
    else:
        brands = Brand.objects.all()
        return render(request, 'index.html', context={'brands': brands})


def create_user(request):
    if request.user.is_authenticated and request.user.is_superuser and request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']
        email = data['email']
        user = User.objects.create_user(username, password, email)
        user.save()
    else:
        return JsonResponse('This malicious attempt to login is reported.')


def subscribe(request):
    pass


def contact(request):
    brands = Brand.objects.all()
    categories = Category.objects.all()
    return render(request, template_name='contact.html', context={'brands': brands, 'categories': categories})
