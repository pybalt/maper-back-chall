from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method='get', responses={200: 'OK'})
@api_view(['GET'])
def ok(request):
    return Response('OK')