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
    
    def put(self, request):
        email = Email.objects.get(pk=request.data['id'])
        serializer = EmailSerializer(email, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        email = Email.objects.get(pk=request.data['id'])
        user_email = email.email
        email.delete()
        return Response({"message":f"{user_email} deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
