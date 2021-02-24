from typing import Any

from rest_framework.request import Request
from rest_framework.permissions import BasePermission


class HasAdminAccount(BasePermission):
    def has_permission(self, request: Request, view: Any):
        return request.user.is_admin_account


class HasStaffAccount(BasePermission):
    def has_permission(self, request: Request, view: Any):
        return request.user.is_staff_account


class HasAgentAccount(BasePermission):
    def has_permission(self, request: Request, view: Any):
        return request.user.is_agent_account


class HasBasicAccount(BasePermission):
    def has_permission(self, request: Request, view: Any):
        return request.user.is_basic_account
