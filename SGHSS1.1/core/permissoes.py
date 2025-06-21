from rest_framework import permissions

class IsAdministradorTotal(permissions.BasePermission):
    """
    Permite acesso total apenas ao Administrador com permissão TOTAL.
    """
    def has_permission(self, request, view):
        user = getattr(request, 'user', None)
        return bool(user and hasattr(user, 'administrador') and user.administrador.permissao == 'Total')


class IsAdministradorParcial(permissions.BasePermission):
    """
    Permite acesso parcial apenas ao Administrador com permissão PARCIAL.
    """
    def has_permission(self, request, view):
        user = getattr(request, 'user', None)
        return bool(user and hasattr(user, 'administrador') and user.administrador.permissao == 'Parcial')


class IsProfissional(permissions.BasePermission):
    """
    Permite acesso apenas a usuários que são profissionais.
    """
    def has_permission(self, request, view):
        user = getattr(request, 'user', None)
        return bool(user and hasattr(user, 'profissional'))


class IsReadOnly(permissions.BasePermission):
    """
    Permissão somente para leitura.
    """
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class ProntuarioPermission(permissions.BasePermission):
    """
    Profissionais podem ler, criar e atualizar Prontuários.
    Mas não podem deletar.
    """
    def has_permission(self, request, view):
        user = getattr(request, 'user', None)
        if request.method in ['DELETE']:
            return False
        return bool(user and hasattr(user, 'profissional'))

    def has_object_permission(self, request, view, obj):
        if request.method in ['DELETE']:
            return False
        return True
    