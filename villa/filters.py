import django_filters
from .models import Villa


class VillaFilters(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = Villa
        fields = ('category',
                  'area',
                  'material',
                  'security',
                  'floor_number',
                  'bedroom',
                  'bathroom',
                  'parking_space_capacity',
                  'payment_method'
                  )
