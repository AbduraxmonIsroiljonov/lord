from rest_framework import serializers
from main.models import *


class NewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewPosts
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "type", "name"]


class LastestVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastestVideos
        fields = "__all__"


class TopPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopPosts
        fields = "__all__"


class TrendyPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendyPosts
        fields = "__all__"


class MegaNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MegaNews
        fields = "__all__"


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class SocialNetworksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetworks
        fields = "__all__"


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = "__all__"


class NewCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewComments
        fields = "__all__"


class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        models = EditProfile
        fields = "__all__"


class SendPostSerializer(serializers.ModelSerializer):
    class Meta:
        models = SendPost
        fields = "__all__"


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        models = Writer
        fields = "__all__"


class ReletedPostsSerializer(serializers.ModelSerializer):
    class Meta:
        models = ReletedPosts
        fields = "__all__"


class LoginPageSerializer(serializers.ModelSerializer):
    class Meta:
        models = LoginPage
        fields = "__all__"


class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        models = NewsLetter
        fields = "__all__"


class PopularPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularPosts
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class PostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostType
        fields = "__all__"