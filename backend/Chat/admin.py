from django.contrib import admin
from Chat.models import Ticket, Conversation


class ConversationAdmin(admin.ModelAdmin):
    list_display = ('account', 'second_account', 'is_seen_account', 'is_seen_second_account')

admin.site.register(Conversation, ConversationAdmin)



class TicketAdmin(admin.ModelAdmin):
    list_display = ('conversation', 'account', 'text')

admin.site.register(Ticket, TicketAdmin)
