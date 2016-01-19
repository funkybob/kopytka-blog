from django.db.models.functions import Now

from array_tags.managers import TagQuerySet


class PostQuerySet(TagQuerySet):
    def published(self):
        return self.filter(is_published=True)

    def current(self):
        return self.filter(
            live_date__lte=Now(),
            is_published=True,
        ).exclude(
            kill_date__lte=Now(),
        ).select_related('posted_by')
