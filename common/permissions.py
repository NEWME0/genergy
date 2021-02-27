from typing import Any

from rest_framework.request import Request
from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsAdminUser(BasePermission):
    def has_permission(self, request: Request, view: Any):
        return request.user.is_admin_account


class IsStaffUser(BasePermission):
    def has_permission(self, request: Request, view: Any):
        return request.user.is_staff_account


class IsAgentUser(BasePermission):
    def has_permission(self, request: Request, view: Any):
        return request.user.is_agent_account


class IsBasicUser(BasePermission):
    def has_permission(self, request: Request, view: Any):
        return request.user.is_basic_account
