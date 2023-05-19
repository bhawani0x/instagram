from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=200)

    def __str__(self):
        return self.tag_name


class Photo(models.Model):
    photo_name = models.CharField(max_length=50)
    insta_post = models.ImageField(upload_to="insta-post/%Y/%m/%d", null=True)
    post_category = models.ManyToManyField(Category)
    post_tag = models.ManyToManyField(Tag)
    post_like = models.CharField(max_length=50)

    def __str__(self):
        return self.photo_name
