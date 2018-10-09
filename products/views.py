from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.authentication import BasicAuthentication
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny

from ockydocky_backend.authentication import CsrfExemptSessionAuthentication
from products import models as pm, serializers as ps


class CategoryListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """ Listing viewset for categories"""
    permission_classes = (AllowAny, )
    serializer_class = ps.CategoryModelSerializer
    queryset = pm.Category.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = ('title', )
    search_fields = ('title', )


class SubCategoryListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """ Listing ViewSet for Subcategories"""
    permission_classes = (AllowAny, )
    serializer_class = ps.SubCategoryModelSerializer
    queryset = pm.SubCategory.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = ('title', )
    filter_fields = ('category', )
    search_fields = ('title', )


class ProductListCreateViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """ Product Listing view"""
    permission_classes = (AllowAny, )
    queryset = pm.Product.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = ('title',)
    search_fields = ('title',)
    filter_fields = ('sub_category', 'sub_category__category')
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_serializer_class(self):
        """ Seperate serializer for create and list"""
        serializer_class = ps.ProductListModelSerializer
        if self.action == 'create':
            serializer_class = ps.ProductCreateModelSerializer

        return serializer_class
