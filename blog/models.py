from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #author : 추후 작성 예정
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'