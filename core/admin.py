from django.contrib import admin
from .models import News, TeamMember, Partner, HistoryLine, NewsImage

class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1 # Сколько пустых форм для добавления показать по умолчанию
    fields = ['image', 'order']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'display_style')
    search_fields = ('title', 'content')
    inlines = [NewsImageInline] # Добавляем инлайн для управления фотографиями

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'role')
    search_fields = ('last_name', 'first_name', 'role')

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(HistoryLine)
class HistoryLineAdmin(admin.ModelAdmin):
    list_display = ('title', 'years', 'location')
    search_fields = ('title', 'description')
