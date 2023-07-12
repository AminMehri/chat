from rest_framework.permissions import BasePermission, SAFE_METHODS
from Admin.models import Admin
from Account.models import Account


class IsVerify(BasePermission):
    def has_permission(self, request, view):
        self.message = 'شما ایمیل خودرا تایید نکرده اید.'
        if Account.objects.filter(user=request.user, email_verified=False).exists():
            return False
        return bool(request.user and request.user.is_authenticated)



class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        self.message = 'شما قابلیت دسترسی به این بخش را ندارید.'
        if not Admin.objects.filter(user__user=request.user).exists():
            return False
        admin = Admin.objects.get(user__user=request.user)
        return bool(request.user and admin.admin_rule == 'superuser')



class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        self.message = 'شما قابلیت دسترسی به این بخش را ندارید.'
        if not Admin.objects.filter(user__user=request.user).exists():
            return False
        admin = Admin.objects.get(user__user=request.user)
        return bool(request.user and (admin.admin_rule == 'admin' or admin.admin_rule == 'superuser'))