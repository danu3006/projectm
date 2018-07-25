# from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from itemsdb import models as itemsdb_models
from .serializers import ItemSerializer


# class ActiveItemListAPIHandler(generics.ListAPIView):
#     """ Handles all API functionality for listing active items. """
#
#     queryset = itemsdb_models.Item.objects.filter(active=True)
#     serializer_class = ItemSerializer
#     permission_classes = (IsAdminUser, )


class ActiveItemListAPIHandler(APIView):
    permission_classes = (IsAdminUser,)
    serializer_class = ItemSerializer

    def get(self, request):
        return Response(self.serializer_class(itemsdb_models.Item.objects.filter(active=True), many=True).data)

    def post(self, request):
        slug = request.POST.get('category')
        json = self.serializer_class(itemsdb_models.Item.objects.filter(category__slug=slug, active=True), many=True)
        return Response(json.data)
