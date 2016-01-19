import re

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from array_tags.fields import TagField

from . import managers


class Post(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(max_length=200)
    content = models.TextField(blank=True)

    created = models.DateTimeField(default=timezone.now, editable=False)
    live_date = models.DateTimeField(_('Post goes live at'), default=timezone.now)
    kill_date = models.DateTimeField(_('Post expires at'), default=None, null=True, blank=True)
    is_published = models.BooleanField(_('Is Published?'), default=False, db_index=True)

    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    tags = TagField(lower=True)

    objects = managers.PostQuerySet.as_manager()

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return self.title

    def auto_tag(self, taglist=None):
        '''
        Add tags according to all available tags.
        '''
        if taglist is None:
            taglist = {
                word.lower()
                for word in Post.objects.all_tag_values('tags')
            }
        words = {
            word.strip().lower()
            for word in re.split(r'(\W+)', self.content)
        }
        self.tags += list(words.intersection(taglist))
