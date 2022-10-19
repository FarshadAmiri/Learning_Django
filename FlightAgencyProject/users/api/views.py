from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response


class UserInfoAPI(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        return Response(data={'username': request.user.username,
                              'email': request.user.email,
                              'first name': request.user.first_name,})


class UserLogoutAPI(GenericAPIView):
    permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(data={'message': f"bye {request.user.first_name}"})