from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone

from communication.forms import MessageForm
from communication.models import Messages
from django.views.generic import ListView, DetailView, RedirectView, FormView

from users.models import UserTable


class MessagesListView(LoginRequiredMixin, ListView):
    model = Messages

    def get_queryset(self):
        return Messages.objects.filter(receiver=self.request.user).values("sender").distinct().annotate()


class MessagesDetailView(LoginRequiredMixin, ListView):
    model = Messages
    # template_name = ""  TEMPLATE EKLENECEK

    def get_queryset(self):
        super().get_queryset().filter(
            Q(sender_id=self.kwargs["user_id"], receiver=self.request.user) & Q(seen__isnull=True)
        ).update(seen=timezone.now())
        query =super().get_queryset().filter(
            Q(sender_id=self.kwargs["user_id"], receiver=self.request.user) |
            Q(receiver_id=self.kwargs["user_id"], sender=self.request.user)
        ).order_by("created")
        total = query.count()
        limit = 50
        offset = total - limit if total - limit > 0 else 0
        return query[offset:]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["other_user"] = UserTable.objects.get(id=self.kwargs["user_id"])
        context["form"] = MessageForm()
        return context


class MessagesSendView(LoginRequiredMixin, FormView):
    form_class = MessageForm

    def get_success_url(self):
        return reverse("messages_detail", kwargs={"user_id": self.kwargs["user_id"]})

    def form_valid(self, form):
        Messages.objects.create(
            sender=self.request.user,
            receiver_id=self.kwargs["user_id"],
            message=form.cleaned_data["message"],
            file=form.cleaned_data["file"]
        )
        return super().form_valid(form)
