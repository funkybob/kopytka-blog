from django.views import generic

from . import models


class PostMixin:
    model = models.Post

    def get_queryset(self):
        tags = [
            tag.strip().lower()
            for tag in self.request.GET.getlist('tags')
        ]
        return super().get_queryset().current().filter(tags__contains=tags)


class PostList(PostMixin, generic.ListView):
    allow_empty = True
    paginate_by = 12

    def get_context_data(self, **kwargs):
        tag_counts = self.object_list.count_tag_values('tags')
        most_common = sorted(tag_counts.items(), key=lambda x: x[1])
        return super().get_context_data(most_common=most_common, **kwargs)


class PostDetail(PostMixin, generic.DetailView):
    most_like = 6

    def get_context_data(self, **kwargs):
        most_like = self.get_queryset().most_like('tags', self.object.tags)[self.most_like:]
        return super().get_context_data(most_like=most_like, **kwargs)