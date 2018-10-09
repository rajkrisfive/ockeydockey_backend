from django.conf.urls import url

from rest_framework.routers import SimpleRouter

from products import views as pv

router = SimpleRouter()
router.register(r'category-list', pv.CategoryListViewSet, base_name='category-list')
router.register(r'sub-category-list', pv.SubCategoryListViewSet, base_name='sub-category-list')
router.register(r'product-list-create', pv.ProductListCreateViewSet, base_name='product-list-create')

urlpatterns = []

urlpatterns += router.urls