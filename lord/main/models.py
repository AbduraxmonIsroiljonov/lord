from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Category(models.Model):
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=155)


class PostType(models.Model):
    name = models.CharField(max_length=255)


class Account(models.Model):
    photo = models.ImageField()
    nick_name = models.CharField(max_length=255, primary_key=True)


class PopularPosts(models.Model):
    video = models.ImageField()
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    founder = models.ForeignKey(Account, on_delete=models.CASCADE)
    posted_date = models.DateTimeField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class NewPosts(models.Model):
    video = models.ImageField()
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    founder = models.ForeignKey(Account, on_delete=models.CASCADE)
    posted_date = models.DateTimeField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class LastestVideos(models.Model):
    video = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class TrendyPosts(models.Model):
    video = models.ImageField()
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    founder = models.ForeignKey(Account, on_delete=models.CASCADE)
    posted_date = models.DateTimeField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class TopPosts(models.Model):
    video = models.ImageField()
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    founder = models.ForeignKey(Account, on_delete=models.CASCADE)
    posted_date = models.DateTimeField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class MegaNews(models.Model):
    text = models.CharField(max_length=255)
    title = models.CharField(max_length=255)


class NewsLetter(models.Model):
    letter = models.CharField(max_length=255)


class Categories(models.Model):
    name = models.CharField(max_length=255)


class SocialNetworks(models.Model):
    accounts = models.CharField(max_length=255)


class LoginPage(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)


class NewComments(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)


class Follow(models.Model):
    nickname = models.CharField(max_length=255)
    photo = models.ImageField()


class MegaNews(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class ReletedPosts(models.Model):
    video = models.ImageField()
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    founder = models.ForeignKey(Account, on_delete=models.CASCADE)
    posted_date = models.DateTimeField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class FollowMe(models.Model):
    nickname = models.CharField(max_length=255)
    photo = models.ImageField()
    name = models.CharField(max_length=255)


class Writer(models.Model):
    nickname = models.CharField(max_length=255)
    photo = models.ImageField()
    name = models.CharField(max_length=255)


class LastestPosts(models.Model):
    video = models.ImageField()
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    founder = models.ForeignKey(Account, on_delete=models.CASCADE)
    posted_date = models.DateTimeField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class CategorySport(models.Model):
    posts = models.ForeignKey(ReletedPosts, on_delete=models.CASCADE,)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class SendPost(models.Model):
    title = models.CharField(max_length=255)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    image = models.ImageField()


class EditProfile(models.Model):
    first_name = models.CharField(max_length=255)
    lasst_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    old_password = models.CharField(max_length=255)
    new_password = models.CharField(max_length=255)
    email = models.EmailField()
    banner = models.ImageField()
    image = models.ImageField()
    text = models.CharField(max_length=255)
    color = models.ImageField()
    align = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
