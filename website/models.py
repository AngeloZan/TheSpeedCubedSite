from django.db import models

class FeedbackModel(models.Model):
    name = models.CharField(max_length=600, default='')
    contact = models.CharField(max_length=600, default='')
    message = models.CharField(max_length=600, default='')
    send_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


