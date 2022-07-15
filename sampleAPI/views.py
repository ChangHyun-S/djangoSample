from rest_framework.response import Response
from rest_framework.decorators import api_view
from library.DB import connection, request_data
from library.json import jsons
from .querystring import *


@api_view(['GET'])
def test(request):
    if request.method == 'GET':
        return test_api(request)


def test_api(request):
    params = request_data(request)

    with connection() as cursor:
        if 'name' in params:
            cursor.execute(insert_usertable(), params)

        cursor.execute(select_usertable(), params)
        data = jsons(cursor)

    return Response(data=data)
