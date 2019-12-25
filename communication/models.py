from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class UserComments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                             related_name='comments_to_me', verbose_name=_("User"))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                              related_name='comments_by_me', verbose_name=_("Owner"))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', blank=True, null=True,
                               verbose_name=_("Parent"))
    comment = models.TextField(max_length=140, verbose_name=_("Comment"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    image = models.ImageField(blank=True, null=True, verbose_name=_("Image"))


def determine_message_file(instance, filename):
    low = min([instance.sender.id, instance.receiver.id])
    high = max([instance.sender.id, instance.receiver.id])
    return f"messages/{low}_{high}/{filename}"


class Messages(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                               related_name='messages_from_me', verbose_name=_("Sender"))
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                 related_name='messages_to_me', verbose_name=_("Receiver"))
    message = models.TextField(max_length=140, verbose_name=_("Message"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    seen = models.DateTimeField(blank=True, null=True, verbose_name=_("Seen"))
    file = models.FileField(blank=True, null=True, upload_to=determine_message_file, verbose_name=_("File"))

    class Meta:
        permissions = (
            ("can_send", _("Can send message")),
        )

    def __str__(self):
        return f"<Message id={self.id} sender={self.sender.username} receiver={self.receiver.username}>"