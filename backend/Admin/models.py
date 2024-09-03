from django.db import models
from Account.models import Account


class Admin(models.Model):
    ADMIN_RULE = (
        ("superuser", "superuser"),
        ("admin", "admin"),
    )
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    admin_rule = models.CharField(choices=ADMIN_RULE, max_length=15, default='admin')

    def __str__(self):
        return self.user.user.username