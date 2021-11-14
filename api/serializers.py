from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from article.models import Article
from user.models import User


class AuthorUserNameSerializer(serializers.RelatedField):
    def to_representation(self,value):
        return value.username

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','username']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ArticleSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    # author = UserSerializer()
    # author = serializers.HyperlinkedIdentityField(view_name='api:authors')
    # author = AuthorUserNameSerializer(read_only=True)
    # author = serializers.CharField(source="author.username",read_only=True)
    author = serializers.SerializerMethodField('get_author')

    class Meta:
        model = Article
        # fields = ['author','title','slug','category','describtion','picture','video','publish','status','is_special']
        # fields = '__all__'
        exclude = ['hits']

    # def validate_title(self, title):
    #     words = ('crypto','wallet','hash')

    #     for word in words:
    #         if word in title.lower():
    #             raise serializers.ValidationError('this word "{}" is forbidden'.format(word))
    
    # def validate(self,data):
    #     if data['title'] != data['slug']:
    #         raise serializers.ValidationError("title not equal to slug")
    #     return data


    def get_author(self,obj):
        return {
            'username' : obj.author.username,
            'first_name' : obj.author.first_name,
            'last_name' : obj.author.last_name,            
            }