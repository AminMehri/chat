from django.db import models
from Account.models import Account
from django.utils import timezone
from Admin.models import Admin


class Conversation(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    second_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="conv")
    is_seen_account = models.BooleanField(default=False)
    is_seen_second_account = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField()

    def __str__(self):
        return self.account.user.username + ' ' + self.second_account.user.username



class Ticket(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=2048)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.conversation.account.user.username + ' ' + self.conversation.second_account.user.username   
