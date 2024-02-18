from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from metrics.models import MachineRuntime, Measurement
from metrics.serializers import MachineRuntimeSerializer, MeasurementSerializer
from .serializers import MachineRuntimeRequestSerializer, SensorDataRequestSerializer
from .swagger_params import page_size_param, page_param, sensors_param, start_date_param, end_date_param
from .pagination import SensorDataPagination

@swagger_auto_schema(method='post', request_body=MachineRuntimeRequestSerializer, responses={200: MachineRuntimeSerializer, 404: 'No data found', 400: 'Bad request'})
@api_view(['POST'])
def machine_runtime(request):
    """
    View function to retrieve machine runtime data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        Response: The HTTP response object containing the serialized machine runtime data.

    Raises:
        MachineRuntime.DoesNotExist: If no machine runtime data is found.

    """
    request_serializer = MachineRuntimeRequestSerializer(data=request.data)

    if not request_serializer.is_valid():
        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        machine_id = request_serializer.validated_data['machine_id']
        date = request_serializer.validated_data['date']

        try:
            runtime = MachineRuntime.objects.get(machine_id=machine_id, date=date)
            serializer = MachineRuntimeSerializer(runtime)
            return Response(serializer.data, content_type='application/json', status=status.HTTP_200_OK)
        except MachineRuntime.DoesNotExist:
            return Response('No data found', status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(method='get',
                    responses={
                        200: MeasurementSerializer(many=True, help_text='List of sensor data'),
                        404: 'No data found',
                        400: 'Bad request'},
                    manual_parameters=[
                        page_size_param,
                        page_param,
                        start_date_param,
                        end_date_param,
                        sensors_param
                        ]
                    )
@api_view(['GET'])
def sensor_data(request):
    """
    Retrieve sensor data based on the provided parameters.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        Response: The HTTP response containing the sensor data.

    Raises:
        NotFound: If no data is found for the given parameters.
    """

    request_serializer = SensorDataRequestSerializer(data=request.query_params)

    request_serializer.sensors = list(map(int, request.query_params.get('sensors').split(',')))
    
    if not request_serializer.is_valid():
        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        sensors = request_serializer.validated_data['sensors']
        start_date = request_serializer.validated_data['start_date']
        end_date = request_serializer.validated_data['end_date']

        try:
            paginator = SensorDataPagination()
            measurements = Measurement.objects.filter(sensor_id__in=sensors, date__range=[start_date, end_date])
            page = paginator.paginate_queryset(measurements, request)
            serializer = MeasurementSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Measurement.DoesNotExist:
            return Response('No data found', status=status.HTTP_404_NOT_FOUND)