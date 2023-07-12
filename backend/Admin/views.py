from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from Admin.permissions import IsSuperUser, IsAdminUser
from Account.models import Account, User
from Admin.models import Admin
from Chat.models import Conversation, Ticket
from datetime import datetime
from Admin.serializers import AddConversationSerializer
import traceback
from django.utils import timezone



def error_text(error_obj):
    text = "مقادیر نادرست برای:"
    for field, reason in error_obj.items():
        text += f"\n{field}: {reason[0]}"
    return text



class ShowUsers(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get(self, request):
        try:
            accounts = Account.objects.all().order_by('-created_at')

            data = []
            for account in accounts:
                data.append({
                    'username': account.user.username,
                    'email_verified': account.email_verified,
                    'created_at': account.created_at,
                })
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(str(e), status=status.HTTP_418_IM_A_TEAPOT)



class ShowAdminUsers(APIView):
    permission_classes = (IsAuthenticated, IsSuperUser)

    def get(self, request):
        try:
            admins = Admin.objects.all()

            data = []
            for admin in admins:
                data.append({
                    'admin': admin.user.user.username,
                    'admin_rule': admin.admin_rule 
                })
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(str(e), status=status.HTTP_418_IM_A_TEAPOT)



class AddAdmin(APIView):
    permission_classes = (IsAuthenticated, IsSuperUser)

    def post(self, request):
        try:
            username = request.data.get("username")

            if not Account.objects.filter(user__username=username).exists():
                return Response({"message": "user not found!"}, status=status.HTTP_404_NOT_FOUND)

            account = Account.objects.get(user__username=username)

            if Admin.objects.filter(user=account).exists():
                return Response({"message": "already is an admin"}, status=status.HTTP_208_ALREADY_REPORTED)

            Admin.objects.create(user=account, admin_rule='admin')
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(str(e), status=status.HTTP_418_IM_A_TEAPOT)



class RemoveAdmin(APIView):
    permission_classes = (IsAuthenticated, IsSuperUser)

    def post(self, request):
        try:
            username = request.data.get("username")

            if not Account.objects.filter(user__username=username).exists():
                return Response({"message": "user not found!"}, status=status.HTTP_404_NOT_FOUND)

            account = Account.objects.get(user__username=username)

            if not Admin.objects.filter(user=account).exists():
                return Response({"message": "admin not found!"}, status=status.HTTP_404_NOT_FOUND)

            if Admin.objects.filter(user=account, admin_rule='superuser').exists():
                return Response({"message": "request is not acceptable!"}, status=status.HTTP_406_NOT_ACCEPTABLE)
                
            Admin.objects.filter(user=account).delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(str(e), status=status.HTTP_418_IM_A_TEAPOT)



class ShowAllConversations(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get(self, request):
        conversations = Conversation.objects.all().order_by('-last_update')

        data = []
        for conversation in conversations:
            data.append({
                'id': conversation.id,
                'account': conversation.account.user.username,
                'second_account': conversation.second_account.user.username,
                'is_seen_account': conversation.is_seen_account,
                'is_seen_second_account': conversation.is_seen_second_account,
                'created_at': datetime.strftime(conversation.created_at, "%Y-%m-%d %H:%M"),
                'last_update': datetime.strftime(conversation.last_update, "%Y-%m-%d %H:%M"),
            })
        
        return Response(data, status=status.HTTP_200_OK)



class ShowAllTickets(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get(self, request):
        tickets = Ticket.objects.all().order_by('conversation').order_by('-created_at')

        data = []
        for ticket in tickets:
            data.append({
                'id': ticket.id,
                'conversation_id': ticket.conversation.id,
                'coversation_users': ticket.conversation.account.user.username + ' ' + ticket.conversation.second_account.user.username,
                'sender': ticket.account.user.username,
                'text': ticket.text,
                'created_at': datetime.strftime(ticket.created_at, "%Y-%m-%d %H:%M")
            })

        return Response(data, status=status.HTTP_200_OK)



class SendTicket(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request):
        try:
            serializer = AddConversationSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({"message": "مقادیر به درستی وارد نشده", "detail": error_text(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)

            # Show failded message
            failed = []

            text = serializer.data.get('text')
            # users who want to send ticket to them
            users_id = serializer.data.get('usersId').split()
            for id in users_id:
                if not Account.objects.filter(user=request.user).exists() or not Account.objects.filter(user__id=id).exists():
                    failed.append({'id': id, 'message': 'user does not exist!'})
                    continue
                account = Account.objects.get(user=request.user)
                another_account = Account.objects.get(user__id=id)

                if account == another_account:
                    failed.append({'id': id, 'message': 'you cant send message to your self!'})
                    continue

                # check for existing coversation
                if Conversation.objects.filter(account=account, second_account=another_account).exists():
                    Conversation.objects.filter(account=account, second_account=another_account).update(is_seen_account=True, is_seen_second_account=False, last_update=timezone.now())
                    conversation = Conversation.objects.get(account=account, second_account=another_account)
                elif Conversation.objects.filter(account=another_account, second_account=account).exists():
                    Conversation.objects.filter(account=another_account, second_account=account).update(is_seen_account=False, is_seen_second_account=True, last_update=timezone.now())
                    conversation = Conversation.objects.get(account=another_account, second_account=account)
                else:
                    conversation = Conversation.objects.create(account=account, second_account=another_account, is_seen_account=True, is_seen_second_account=False, last_update=timezone.now())
                Ticket.objects.create(conversation=conversation, text=text, account=account)

            return Response(failed, status=status.HTTP_201_CREATED)
        except Exception:
            traceback.print_exc()
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
