from django.contrib import admin
from .models import Attribute, Choice, Score, AttributeScore
from django import forms

# Register your models here.
class AttributeModelForm(forms.ModelForm):
    ATTRIBUTETYPE_CHOICES = (
        ('sentiment', 'sentiment'),
        ('infostartup', 'infostartup'),
        ('infoplatform', 'infoplatform'),
    )
    attributetype = forms.ChoiceField(choices=ATTRIBUTETYPE_CHOICES)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'attributetype')
    form = AttributeModelForm
admin.site.register(Attribute, AttributeAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('label', 'value')
admin.site.register(Choice, ChoiceAdmin)

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('startupname', 'productname', 'totalscore', 'scorecategory','status', 'changeby', 'changetime', 'calculatedate')
admin.site.register(Score, ScoreAdmin)

class AttributeScoreAdmin(admin.ModelAdmin):
    list_display = ('score', 'attributetype','name', 'value')
    ordering = ('score','-attributetype', 'name')
admin.site.register(AttributeScore, AttributeScoreAdmin)

admin.site.site_header = "SurPre Admin"
admin.site.site_url = "/surpre"