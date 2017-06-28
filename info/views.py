from django.shortcuts import render
from profiles.models import Product, Profile, Material


def info(request):
    return render(request, 'info.html', {'profiles': Profile.objects.all(),
                                         'products': Product.objects.all(),
                                         'products_amounts': return_product_amount(Product.objects.all())})


def return_product_amount(products):
    quantidades = Material.objects.all()
    cafe = quantidades[0]
    acucar = quantidades[1]
    qcafe = cafe.quantidade
    qacucar = acucar.quantidade
    amounts = {}
    for product in products:
        if product.id == 3:
            amounts[product.name] = int(qcafe/5)
        if product.id == 4:
            value = [qcafe / 5, qacucar / 5]
            amounts[product.name] = int(min(value))
    return amounts
