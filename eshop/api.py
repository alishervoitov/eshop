from rest_framework.routers import DefaultRouter
from product.api_views import ProductViewset

router = DefaultRouter()

router.register('products', ProductViewset, basename='products')