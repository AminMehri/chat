from rest_framework.permissions import BasePermission, SAFE_METHODS
from Admin.models import Admin
from Account.models import Account


class IsVerify(BasePermission):
    def has_permission(self, request, view):
        self.message = 'you don not confirm your email'
        if Account.objects.filter(user=request.user, email_verified=False).exists():
            return False
        return bool(request.user and request.user.is_authenticated)



class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        self.message = 'you do not able to access here'
        if not Admin.objects.filter(user__user=request.user).exists():
            return False
        admin = Admin.objects.get(user__user=request.user)
        return bool(request.user and admin.admin_rule == 'superuser')



class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        self.message = 'you do not able to access here'
        if not Admin.objects.filter(user__user=request.user).exists():
            return False
        admin = Admin.objects.get(user__user=request.user)
        return bool(request.user and (admin.admin_rule == 'admin' or admin.admin_rule == 'superuser'))