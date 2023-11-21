from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from webapi.models import Record
from webapi.serializers import RecordSerializer


@api_view(['GET',])
def get_record(request, date_record):
    if request.method == 'GET':
        record = Record.objects.get(date_record=date_record)
        serializer = RecordSerializer(record, many=False)
        return Response(serializer.data)
