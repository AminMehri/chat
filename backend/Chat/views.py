from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from Admin.permissions import IsVerify
from Account.models import Account
from Chat.serializers import CreateConversationSerializer, AddTicketSerializer
from Chat.models import Conversation, Ticket
import traceback
from itertools import chain
from datetime import datetime


def error_text(error_obj):
    text = "مقادیر نادرست برای:"
    for field, reason in error_obj.items():
        text += f"\n{field}: {reason[0]}"
    return text



class ConversationView(APIView):
    permission_classes = (IsAuthenticated, IsVerify)

    def get(self, request):
        try:
            account = Account.objects.get(user=request.user)

            data = []
            username = ''
            is_seen = False

            conversation_account = Conversation.objects.filter(account__user=request.user)
            conversation_another_account = Conversation.objects.filter(second_account__user=request.user)         

            conversations = sorted(chain(conversation_account, conversation_another_account), key=lambda instance: instance.last_update, reverse=True)

            for conver in conversations:

                try:
                    c = Conversation.objects.get(id=conver.id)
                    mes = Ticket.objects.filter(conversation=c).order_by('-created_at')[:1]
                    for m in mes:
                        message = m.text
                        sender = m.account
                except Exception as E:
                    print(E)
                    message = ''
                
                if account == sender:
                    last_by_me = True
                else: 
                    last_by_me = False

                if account == conver.account:
                    username = conver.second_account.user.username
                    is_seen = conver.is_seen_account
                    contact_seen = conver.is_seen_second_account
                
                if account == conver.second_account:
                    username = conver.account.user.username
                    is_seen = conver.is_seen_second_account
                    contact_seen = conver.is_seen_account

                data.append({
                    "id": conver.id,
                    "with": username,
                    "last_message": message,
                    "last_by_me": last_by_me,
                    "contact_seen": contact_seen,
                    "is_seen": is_seen,
                    "last_update": datetime.strftime(conver.last_update, "%Y-%m-%d %H:%M"),
                })

            return Response(data)
        
        except Exception:
            traceback.print_exc()
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        try:
            serializer = CreateConversationSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({"message": "مقادیر به درستی وارد نشده", "detail": error_text(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)

            text = serializer.data.get('text')
            username = serializer.data.get('another_account')

            if not Account.objects.filter(user=request.user).exists() or not Account.objects.filter(user__username=username).exists():
                return Response({"message": "user not found!"}, status=status.HTTP_404_NOT_FOUND)

            account = Account.objects.get(user=request.user)
            another_account = Account.objects.get(user__username=username)

            if account == another_account:
                return Response({"message": "you can't start chat with your self"}, status=status.HTTP_406_NOT_ACCEPTABLE)

            if Conversation.objects.filter(account=account, second_account=another_account).exists() or Conversation.objects.filter(account=another_account, second_account=account).exists():
                return Response({"message": "chat is already exist!"}, status=status.HTTP_208_ALREADY_REPORTED)
            else:
                conversation = Conversation.objects.create(account=account, second_account=another_account, is_seen_account=True, is_seen_second_account=False, last_update=timezone.now())
            Ticket.objects.create(conversation=conversation, text=text, account=account)

            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            traceback.print_exc()
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class TicketView(APIView):
    permission_classes = (IsVerify, )

    def get(self, request):
        try:
            conversationId = request.query_params.get("id")

            if not Conversation.objects.filter(id=conversationId, account__user=request.user).exists():
                if not Conversation.objects.filter(id=conversationId, second_account__user=request.user).exists():
                    return Response({"message": "بحث موردنظر یافت نشد"}, status=status.HTTP_404_NOT_FOUND)

            conver = Conversation.objects.get(id=conversationId)

            messages = Ticket.objects.filter(conversation=conver).order_by('created_at')

            msgs = []
            for message in messages:
                msgs.append({
                    "sender": message.account.user.username,
                    "text": message.text,
                    "created_at": datetime.strftime(message.created_at, "%Y-%m-%d %H:%M"),  
                })

            account = Account.objects.get(user=request.user)
            if account == conver.account:
                conver.is_seen_account = True
                conver.save()
            if account == conver.second_account:
                conver.is_seen_second_account = True
                conver.save()
            return Response({"messages": msgs})
        except Exception:
            traceback.print_exc()
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        try:
            serializer = AddTicketSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({"message": "مقادیر به درستی وارد نشده", "detail": error_text(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)

            text = serializer.data.get('text')
            conversationId = serializer.data.get('conversationId')

            if not Conversation.objects.filter(id=conversationId, account__user=request.user).exists():
                if not Conversation.objects.filter(id=conversationId, second_account__user=request.user).exists():
                    return Response({"message": "بحث موردنظر یافت نشد"}, status=status.HTTP_404_NOT_FOUND)

            conversation = Conversation.objects.get(id=conversationId)
            conversation.last_update = timezone.now()

            account = Account.objects.get(user=request.user)
            Ticket.objects.create(conversation=conversation, account=account, text=text)

            if account == conversation.account:
                conversation.is_seen_account = True
                conversation.is_seen_second_account = False

            if account == conversation.second_account:
                conversation.is_seen_account = False
                conversation.is_seen_second_account = True
                
            conversation.save()

            return Response(status=status.HTTP_200_OK)
        except Exception:
            traceback.print_exc()
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
