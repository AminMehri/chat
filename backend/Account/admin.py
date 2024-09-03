from django.contrib import admin
from Account.models import User, Account


admin.site.register(User)


class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'email_verified')

admin.site.register(Account, AccountAdmin)