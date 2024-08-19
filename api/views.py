from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Email
from .serializers import EmailSerializer

class EmailView(APIView):
    def get(self, request):
        emails = Email.objects.all()
        serializer = EmailSerializer(emails, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
