from drf_yasg import openapi

page_size_param = openapi.Parameter(
    'page_size',
    in_=openapi.IN_QUERY,
    description='Number of results to return per page',
    type=openapi.TYPE_INTEGER,
    default=10
    )
page_param = openapi.Parameter('page',
    in_=openapi.IN_QUERY,
    description='Page number',
    type=openapi.TYPE_INTEGER,
    default=1)
sensors_param = openapi.Parameter('sensors',
    in_=openapi.IN_QUERY,
    description='List of sensor IDs',
    type=openapi.TYPE_ARRAY,
    items=openapi.Items(type=openapi.TYPE_INTEGER, format=openapi.FORMAT_INT32),
    default=[3348, 2363, 2371, 3356, 3346])
start_date_param = openapi.Parameter('start_date',
    in_=openapi.IN_QUERY,
    description='Start date',
    type=openapi.TYPE_STRING,
    format=openapi.FORMAT_DATE,
    default=("2023-01-30")
    )
end_date_param = openapi.Parameter('end_date',
    in_=openapi.IN_QUERY,
    description='End date',
    type=openapi.TYPE_STRING,
    format=openapi.FORMAT_DATE,
    default=("2024-01-30"))