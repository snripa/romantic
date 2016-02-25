# coding: utf-8

from django import template
from django.core import urlresolvers
from django.core.urlresolvers import reverse, NoReverseMatch
from power_comments.forms import PowerCommentForm
from power_comments.models import PowerComment
from profile.models import CustomUser
from force_blog.models import BlogPost
from materials.models import Material
from info_pages.models import InfoPage


register = template.Library()


@register.inclusion_tag('power_comments/comments.html')
def power_comments(request, app_url, if_comment):
    try:
        profile = CustomUser.objects.get(user=request.user)
    except:
        profile = request.user
    comments = PowerComment.objects.all().filter(app=app_url).order_by('date_creation').exclude(state=0)
    count_comments = comments
    form = PowerCommentForm()
    data = {'comments': comments,
            'app_url': app_url,
            'if_comments': if_comment,
            'count_comments': count_comments,
            'profile': profile,
            'request': request,
            'form': form}
    return data


@register.simple_tag()
def count_inc_power_comments(count_inc):
    if count_inc == None:
        s = '<div class="col-xs-10">'
    else:
        count = int(count_inc)
        total = 10 - int(count_inc)
        s = '<div class="col-xs-%s"></div><div class="col-xs-%s">' % (count, total)
    return s


@register.simple_tag()
def count_power_comments(app_url):
    comments = PowerComment.objects.all().filter(app=app_url).exclude(state=0)
    count_power_comments = comments.count()
    return count_power_comments


@register.simple_tag()
def url_with_comment(app_url):
    id_content = ''.join(filter(lambda x: x.isdigit(), app_url))
    if "blog" in app_url:
        from force_blog.models import BlogPost
        obj = BlogPost.objects.get(id=id_content)
        url = obj.title
    elif "materials" in app_url:
        from materials.models import Material
        try:
            obj = Material.objects.get(id=id_content)
            url = obj.title
        except:
            url = ""
    elif "party" in app_url:
        from party.models import Party
        obj = Party.objects.get(id=id_content)
        url = obj.title
    else:
        url = ""
    return url


@register.simple_tag()
def power_url_edit(obj):
    url = urlresolvers.reverse('admin:%s_%s_change' % (obj._meta.app_label,
                                                       obj._meta.module_name),
                                                       args=[obj.id])
    return url
