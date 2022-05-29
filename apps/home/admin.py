from math import perm
from django.contrib import admin
from .models import TB, Indicateur, Interpretation, Graphe, Donnee
from guardian.admin import GuardedModelAdmin
from guardian.shortcuts import get_objects_for_user

admin.site.register(Donnee)
admin.site.register(Graphe)
admin.site.register(TB)
admin.site.register(Interpretation)

@admin.register(Indicateur)
class IndicateurAdmin(GuardedModelAdmin):
    list_display = ('Intitule_Indicateur',)

    def has_module_permission(self, request):
        if super().has_module_permission(request):
            return True
        return self.get_model_objects(request).exists()

    
    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        return self.get_model_objects(request)

    def has_permission(self, request, obj, action):
        opts = self.opts
        code_name = f'{action}_{opts.model_name}'

        if obj:
            return request.user.has_perm(f'{opts.app_label}.{code_name}', obj)
        else: 
            return True
        
    
    def get_model_objects(self, request, actions=None, klass=None):
        ops = self.opts
        actions = [actions] if actions else ['view', 'edit', 'delete']
        klass = klass or ops.model
        model_name = klass._meta.model_name
        return get_objects_for_user(user=request.user, perms=[f'{perm}_{model_name}' for perm in actions], klass=klass, any_perm=True)


    def has_view_permission(self, request, obj=None):
        return self.has_permission(request, obj, 'view')

    def has_change_permission(self, request, obj=None):
        return self.has_permission(request, obj, 'change')

    def has_delete_permission(self, request, obj=None):
        return self.has_permission(request, obj, 'delete')