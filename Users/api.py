from rest_framework import generics
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
import jwt

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response({"user": UserSerializer(user, context=self.get_serializer_context()).data, "token" : str(RefreshToken.for_user(user))})
       
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        endcoded = jwt.encode(serializer.data, 'secret', algorithm="HS256")
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data, 
            "token" : endcoded
        })
