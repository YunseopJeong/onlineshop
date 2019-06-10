from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from cart.forms import AddProductForm
from .cart import *
# Create your views here.

# 표기 = decorators / import 필요
@require_POST
def add(request, product_id):
    print('장바구니에 넣는 제품 id : ', product_id)

    # cart.py를 import하고 Cart를 빼옴 / Cart(request)  >> 객체생성
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    # 유효한 값이 들어가 있는지 체크
    # input에 들어간 values를 가지고 옴
    form = AddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data

    # 장바구니 추가
    cart.add(product=product, quantity= cd['quantity'], is_update= cd['is_update'])

    # redirect >> 서버에 요청 해달라는 명령
    return redirect('cart:detail')

def detail(request):
    cart = Cart(request)
    for product in cart:
        product['quantity_form'] = AddProductForm(initial={'quantity': product['quantity'], 'is_update': True})
    return render(request, 'cart/detail.html', {'cart': cart})