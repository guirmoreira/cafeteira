from django.shortcuts import render
from django.shortcuts import redirect
from profiles.models import Profile, Product, Orders, Material
from random import *
import json
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AdicionaMaterial

def index(request):
    create_user()
    return render(request, 'index.html', {'profiles': Profile.objects.all(),
                                          'products': Product.objects.all(),
                                          'product_amounts': return_product_amount(Product.objects.all(),
                                                                                   Profile.objects.get(name='Guilherme'))})


def order(request, product="4"):
    token = generate_token()
    include_order_to_db(int(product), token)
    remove_quantidades(int(product))
    return render(request, 'order.html', {'profiles': Profile.objects.all(),
                                          'token': token,
                                          'product': Product.objects.get(pk=int(product))})


def rasp_orders(request):
    undelivered_order = Orders.objects.filter(delivered=False).first()  # retorna o primeiro pedido nao entregue
    order_send = {'token': 0, 'product': 0}
    if undelivered_order is not None:
        order_send['token'] = undelivered_order.token
        order_send['product'] = int(undelivered_order.product)
    else:
        order_send = {}
    data = json.dumps(order_send)
    return HttpResponse(data, content_type='application/json')


def rasp_remove_order(request):
    undelivered_order = Orders.objects.filter(delivered=False).first()  # retorna o primeiro pedido nao entregue
    undelivered_order.delivered = True
    undelivered_order.save()
    return HttpResponse('Order delivered')


def manutencao(request):
    if request.method == 'POST':
        form = AdicionaMaterial(request.POST)
        if form.is_valid():
            quantidades = Material.objects.all()
            qcafe = quantidades[0]
            qacucar = quantidades[1]

            data = form.cleaned_data
            cafe = data['cafe']
            acucar = data['acucar']
            if cafe > 0:
                qcafe.quantidade = qcafe.quantidade + cafe
            if acucar > 0:
                qacucar.quantidade = qacucar.quantidade + acucar
            qcafe.save()
            qacucar.save()
            return redirect('manutencao')
    else:
        form = AdicionaMaterial()

    return render(request, 'manutencao.html', {'products': Product.objects.all(),
                                               'quantidades': Material.objects.all(),
                                               'form': form})


def generate_token():
    token = randrange(1, 255, 1)
    return token


def create_user():
    profiles = Profile.objects.all()
    for profile in profiles:
        profile.delete()
    perfil = Profile(name='Guilherme', email='guilherme@usp.br', cash=6.50)
    perfil.save()


def return_product_amount(products, profile):
    amounts = {}
    for product in products:
        amounts[product.name] = profile.cash/product.price
    return amounts


def include_order_to_db(product, token):
    new_order = Orders(product=product, token=token, delivered=False)
    new_order.save()


def remove_quantidades(product):
    quantia_cafe = 5
    quantia_acucar = 5
    quantidades = Material.objects.all()
    cafe = quantidades[0]
    acucar = quantidades[1]
    if product == 3:
        cafe.quantidade = cafe.quantidade - quantia_cafe
    if product == 4:
        cafe.quantidade = cafe.quantidade - quantia_cafe
        acucar.quantidade = acucar.quantidade - quantia_acucar
    cafe.save()
    acucar.save()
