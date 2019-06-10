from django.shortcuts import render, get_object_or_404

from cart.forms import AddProductForm
from .models import *

# Create your views here.
# 모든 카테고리 출력
# 해당 카테고리 클릭하면 출력
# 입력 값이 없으면 None이 기본값이 된다.
def product_in_category(request, category_slug=None):
    # db검색한 결과를 템플릿에 넘겨줌
    # map형태로 만들어서 넘김
    current_category = None

    # category없이 전체 출력
    categories = Category.objects.all()
    products = Product.objects.filter(available_display = True)

    # category해당하는 것만 출력
    # 없으면 404처리
    if category_slug:
        current_category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category = current_category)

    return render(request, 'shop/list.html', {
                    'current_category' : current_category,
                    'products' : products,
                    'categories' : categories
                    })

# 제품 상세페이지 출력
def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity':1})
    return render(request, 'shop/detail.html', {'product': product, 'add_to_cart':add_to_cart})