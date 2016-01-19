from django.contrib import admin

from . import forms, models


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'live_date', 'kill_date', 'posted_by',)
    list_filter = ('posted_by',)
    date_hierarchy = 'live_date'
    search_fields = ('title', 'content',)
    prepopulated_fields = {'slug': ('title',)}
    form = forms.PostAdminForm

    def queryset(self, request):
        '''
        Limit visible posts to only yours, unless you're superuser.
        '''
        qset = self.model.objects.all()
        if not request.user.is_superuser:
            return qset.filter(posted_by=request.user)
        return qset

    def save_model(self, request, obj, form, change):
        if form.cleaned_data['auto']:
            obj.auto_tag()
        if not change:
            obj.posted_by = request.user
        return super().save_model(request, obj, form, change)

    def auto_tag(self, request, queryset):
        taglist = models.Page.objects.all_tag_values()
        for post in queryset:
            post.auto_tag(taglist)
            post.save()

    actions = [
        auto_tag,
    ]

admin.site.register(models.Post, PostAdmin)
