from django.contrib import admin
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy

from .models import UserComments, Messages


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = (
        "open_link",
        "sender_link",
        "receiver_link",
        "message",
        "file_link",
        "seen",
        "created"
    )
    search_fields = (
        "message__icontains",
        "sender__username__icontains",
        "receiver__username__icontains",
        "file__icontains"
    )
    list_filter = ("created", "seen")
    readonly_fields = ("seen", "created")
    fields = (
        ("sender", "receiver"),
        ("message",),
        ("file",),
        ("created", "seen")
    )
    actions = ("bulk_seen",)

    def bulk_seen(self, request, queryset):
        queryset.update(seen=timezone.now())

    bulk_seen.short_description = gettext_lazy("Set objects to seen now.")

    def open_link(self, obj):
        return mark_safe("<strong>&longrightarrow;</strong>")

    open_link.short_description = gettext_lazy('Open')

    def receiver_link(self, obj):
        link = reverse('admin:users_usertable_change', kwargs={'object_id': obj.receiver.id})
        return mark_safe(f"<a href='{link}'>{obj.receiver}</a>")

    receiver_link.short_description = Messages._meta.get_field('receiver').verbose_name

    def sender_link(self, obj):
        link = reverse('admin:users_usertable_change', kwargs={'object_id': obj.sender.id})
        return mark_safe(f"<a href='{link}'>{obj.sender}</a>")

    sender_link.short_description = Messages._meta.get_field('sender').verbose_name

    def file_link(self, obj):
        if not obj.file:
            return ""
        return mark_safe(f"<a href='{obj.file.url}'>{obj.file.name.split('/')[-1]}</a>")

    sender_link.short_description = Messages._meta.get_field('sender').verbose_name


admin.site.register(UserComments)
