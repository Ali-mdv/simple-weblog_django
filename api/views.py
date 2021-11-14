from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.views.generic.base import TemplateView
from .serializers import ArticleSerializer, UserSerializer ,AuthorSerializer
from .permissions import IsAdminUserOrReadOnly, IsSuperUser ,IsAuthorOrReadOnly, IsSuperUserOrAdminUserReadOnly
from article.models import Article
from django.contrib.sites.models import Site
from user.models import User
from django.contrib.auth import get_user_model
# Create your views here.

# class ArticleListView(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = [IsAdminUserOrReadOnly,]


# class ArticleDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'
#     permission_classes = [IsAuthorOrReadOnly,]


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['is_special', 'status']
    search_fields = ['title', 'describtion','author__first_name','author__last_name']
    ordering_fields = ['status','-created']

    # def get_queryset(self):
    #     queryset = Article.objects.all()
    #     status = self.request.query_params.get('status')
    #     is_special = self.request.query_params.get('is_special')
    #     if status is not None:
    #         queryset = queryset.filter(status=status)

    #     if is_special is not None:
    #         queryset = queryset.filter(is_special=is_special)
    #     return queryset

    def get_permission(self):
        if self.action == 'list':
            permission_classes = [IsAdminUserOrReadOnly,]
        else:
            permission_classes = [IsAuthorOrReadOnly,]


# class UserListView(ListCreateAPIView):
#     # queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsSuperUserOrAdminUserReadOnly,]

#     def get_queryset(self):
#         print(self.request.user)
#         print(self.request.auth)
#         queryset = User.objects.all()
#         return queryset


# class UserDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsSuperUserOrAdminUserReadOnly,]


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUserOrAdminUserReadOnly,]


# class CustomAuthToken(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })


# class RevokeView(APIView):
#     def delete(self, request):
#         request.auth.delete()
#         return Response(status=204)



class GreetView(TemplateView):

    template_name = "registration/rest-auth_greeting.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.get(pk=self.request.user.pk)
        context['site'] = Site.objects.get_current()
        return context



class AuthorView(RetrieveAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = AuthorSerializer