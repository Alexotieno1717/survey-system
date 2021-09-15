from django.contrib import admin
import nested_admin
from .models import Survey, Question, Choice


class ChoiceInLine(nested_admin.NestedTabularInline):
    model = Choice
    extra = 2
    classes = ['collapse']


class QuestionInLine(nested_admin.NestedTabularInline):
    model = Question
    extra = 1
    classes = ['collapse']
    inlines = [ChoiceInLine]


class SurveyAdmin(nested_admin.NestedModelAdmin):
    fieldsets = [
        ('Survey Name', {'fields': ['name']}),
        ('When would you like to publish it?', {'fields': ['published_on'], 'classes': ['collapse']})
    ]
    inlines = [QuestionInLine]
    list_filter = ['published_on']
    search_fields = ['name']


# Register Survey objects along with their nestings and fieldssets with admin
# Other entities need not be registered here since they are already bound to Survey object.
# Participant entity will not be used from admin views. Therefore it is not being registered here.
admin.site.register(Survey, SurveyAdmin)
