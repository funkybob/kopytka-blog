
from django import template
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

import CommonMark

register = template.Library()


@register.filter
def markdown(src):
    return mark_safe(CommonMark.commonmark(force_text(src)))
