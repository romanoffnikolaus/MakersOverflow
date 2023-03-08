from rest_framework.decorators import APIView
from rest_framework.response import Response

from .models import Favorites
from .serializers import FavoritesSerializer
from questions.models import Question


class FavoritesView(APIView):
    def get(self, request):
        queryset = Favorites.objects.filter(user=request.user)
        serializer = FavoritesSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        try:
            favorite = Favorites.objects.get(id=pk)
            favorite.delete()
            return Response(f'Question was deleted')

        except Favorites.DoesNotExist:
            return Response("This question doesn't exists")
