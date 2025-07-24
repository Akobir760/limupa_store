from django.db import models

# Create your models here.

class BasicModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)


class ContactModel(BasicModel):
    name = models.CharField(max_length=123)
    phone_number = models.CharField(max_length=123, null=True, blank=True)
    email = models.EmailField(max_length=123)
    subject = models.CharField(max_length=123)
    message = models.TextField()
    is_read = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} | {self.email}"
    

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"