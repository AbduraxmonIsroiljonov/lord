from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from main.models import *
from main.serializers import *


@api_view("POST")
def create_tag(request):
    serializer = TagSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def list_videos(request):
    videos = LastestVideos.objects.all()
    serializer = LastestVideosSerializer(videos, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_video(request):
    serializer = LastestVideosSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_posts(request):
    posts = TrendyPosts.objects.all()
    serializer = TrendyPostsSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_post(request):
    serializer = TrendyPostsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_top_posts(request):
    top_posts = TopPosts.objects.all()
    serializer = TopPostsSerializer(top_posts, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_top_post(request):
    serializer = TopPostsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_mega_news(request):
    mega_news = MegaNews.objects.all()
    serializer = MegaNewsSerializer(mega_news, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_mega_news(request):
    serializer = MegaNewsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_categories(request):
    categories = Categories.objects.all()
    serializer = CategoriesSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_category(request):
    serializer = CategoriesSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_social_networks(request):
    social_networks = SocialNetworks.objects.all()
    serializer = SocialNetworksSerializer(social_networks, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_social_network(request):
    serializer = SocialNetworksSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_follows(request):
    follows = Follow.objects.all()
    serializer = FollowSerializer(follows, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_follow(request):
    serializer = FollowSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_comments(request):
    comments = NewComments.objects.all()
    serializer = NewCommentsSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_comment(request):
    serializer = NewCommentsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def edit_profile(request):
    EditProfile.objects.create(
        first_name=request.POST.get("first_name"),
        lasst_name=request.POST.get("last_name"),
        user_name=request.POST.get("user_name"),
        old_password=request.POST.get("old_password"),
        new_password=request.POST.get("new_password"),
        email=request.POST.get("email"),
        banner=request.POST.get("banner"),
        image=request.POST.get("image"),
        text=request.POST.get("text"),
        color=request.POST.get("color"),
        align=request.POST.get("align"),
        link=request.POst.get("link"),
    )


@api_view(["GET"])
def list_related_posts(request):
    related_posts = ReletedPosts.objects.all()
    serializer = ReletedPostsSerializer(related_posts, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_related_post(request):
    serializer = ReletedPostsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_newsletters(request):
    newsletters = NewsLetter.objects.all()
    serializer = NewsLetterSerializer(newsletters, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_newsletter(request):
    serializer = NewsLetterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_popular_posts(request):
    popular_posts = PopularPosts.objects.all()
    serializer = PopularPostsSerializer(popular_posts, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_popular_post(request):
    serializer = PopularPostsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_accounts(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_account(request):
    serializer = AccountSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_post_types(request):
    post_types = PostType.objects.all()
    serializer = PostTypeSerializer(post_types, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_post_type(request):
    serializer = PostTypeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
