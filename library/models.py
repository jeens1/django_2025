from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    def __str__(self):
        return f'게시글{self.title}글내용{self.content}-게시날짜{self.created_date}-갱신날짜{self.updated_date}'