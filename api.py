from rest_framework import routers
from login.views import RegisterViewSet, LoginViewSet
from contact.views import ContactViewSet
from product.views import ProductViewset
from checkout.views import CheckoutViewSet

router = routers.DefaultRouter()
router.register(r'register', RegisterViewSet)
router.register(r'login', LoginViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'products', ProductViewset)
router.register(r'checkout', CheckoutViewSet)