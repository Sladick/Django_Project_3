from django import template
from django.db.models import Count, F

from news.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)


@register.inclusion_tag('inc/_sidebar.html')
def show_categories():
    categories = Category.objects.all()
    return {"categories": categories}
