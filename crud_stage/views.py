from rest_framework import generics, status
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from django_filters import rest_framework as filters


class PersonCreateView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
class PersonFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')  # Case-insensitive partial match

    class Meta:
        model = Person
        fields = ['name']

class PersonRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filterset_class = PersonFilter

    def retrieve(self, request, *args, **kwargs):
        lookup_value = kwargs.get('pk_or_name')  # Attempt to retrieve 'pk_or_name' from URL parameters

        if lookup_value is not None:
            queryset = self.get_queryset()
            
            if lookup_value.isdigit():
                # If it's a digit, assume it's a primary key lookup
                queryset = queryset.filter(pk=lookup_value)
            else:
                # If it's not a digit, assume it's a name lookup
                queryset = queryset.filter(name__iexact=lookup_value)

            instance = queryset.first()

            if instance is not None:
                serializer = self.get_serializer(instance)
                return Response(serializer.data)

        return Response({'detail': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        lookup_value = kwargs.get('pk_or_name')  # Attempt to retrieve 'pk_or_name' from URL parameters

        if lookup_value is not None:
            queryset = self.get_queryset()

            if lookup_value.isdigit():
                # If it's a digit, assume it's a primary key lookup
                queryset = queryset.filter(pk=lookup_value)
            else:
                # If it's not a digit, assume it's a name lookup
                queryset = queryset.filter(name__iexact=lookup_value)

            instance = queryset.first()

            if instance is not None:
                serializer = self.get_serializer(instance, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)

        return Response({'detail': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        lookup_value = kwargs.get('pk_or_name')  # Attempt to retrieve 'pk_or_name' from URL parameters

        if lookup_value is not None:
            queryset = self.get_queryset()

            if lookup_value.isdigit():
                # If it's a digit, assume it's a primary key lookup
                queryset = queryset.filter(pk=lookup_value)
            else:
                # If it's not a digit, assume it's a name lookup
                queryset = queryset.filter(name__iexact=lookup_value)

            instance = queryset.first()

            if instance is not None:
                instance.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

        return Response({'detail': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)
