from django.contrib import admin

from webapp.models import Issue, Status, Type



class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'description', 'status')
    list_filter = ('id', 'summary', 'status', 'type')
    search_fields = ('summary', 'status', 'type')
    fields = ('id', 'summary', 'description', 'status')
    readonly_fields = ('id',)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    search_fields = ('title',)
    fields = ('id', 'title')
    readonly_fields = ('id',)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    search_fields = ('title',)
    fields = ('id', 'title')
    readonly_fields = ('id',)


admin.site.register(Issue, IssueAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)
