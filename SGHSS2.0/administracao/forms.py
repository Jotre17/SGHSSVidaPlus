# administracao/forms.py

from django import forms
from django.contrib.auth.models import Group, Permission

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apps_permitidos = ['admin','administracao', 'auth', 'consultas','core','pacientes', 'profissionais','sessions']
        self.fields['permissions'].queryset = Permission.objects.filter(
            content_type__app_label__in=apps_permitidos
        )
