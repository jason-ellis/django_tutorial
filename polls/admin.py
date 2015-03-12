from django.contrib import admin
from polls.models import Choice, Question


# Creates choices admin representation as inline to be used with foreign key
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# Creates question admin screen
class QuestionAdmin(admin.ModelAdmin):
    # Create fieldsets of grouped fields with header, can collapse
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    # Add inline (Choices model) to Questions admin
    inlines = [ChoiceInline]

    # Fields to list on Question admin screen
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # Filter on pub_date added to sidebar
    list_filter = ['pub_date']

    # Adds question text search field
    search_fields = ['question_text']

# Register Question admin under Polls, defined by QuestionAdmin class
admin.site.register(Question, QuestionAdmin)