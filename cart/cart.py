from django.conf import settings
from decimal import Decimal
from shop.models import Product


class Cart(object):

    def __init__(self, request):
        # 세션을 가져온다.
        self.session = request.session

        # CARD_ID key를 가진 세션이 있는지 체크
        # 가져온 세션을 cart라는 변수에 넣는다.(밑에는 로그인 세션을 넣음)
        cart = self.session.get(settings.CART_ID)
        loginid = self.session.get(settings.LOGIN_SESSION_ID)

        print('start-value : ', settings.START + 1)
        print('login-id : ', settings.LOGIN_SESSION_ID)
        # 세션이 없으면, 딕셔너리를 만들어 줘야한다.
        if not cart:
            cart = self.session[settings.CART_ID] = {}

        # 세션이 있으면 딕셔너리를 가지고 온다.
        self.cart = cart

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']

            yield item

    def add(self, product, quantity=1, is_update = False):
        product_id = product.id
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price':str(product.price)}

            if is_update:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.cart[product_id]['quantity'] += quantity

            self.save()

    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del(self.cart[product_id])
            self.save()

    def clear(self):
        self.session[settings.CART_ID] = {}
        self.session.modified = True