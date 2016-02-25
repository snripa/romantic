# coding: utf-8
# author: dlyapun

# from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from profile.models import CustomUser
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render
from django.views.generic import ListView, DetailView
from force_blog.forms import BlogPostForm
from force_blog.models import BlogPost, BlogEdit, Category
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
import time


DISABLE = 0
ENABLE = 1
HOT_POST = 2


class BlogPostListView(ListView):
    model = BlogPost
    context_object_name = 'blog_posts'

    paginate_by = 5

    def get_queryset(self):
        if not self.request.user.is_authenticated():
            qs = BlogPost.objects.select_related('owner', 'owner__user').prefetch_related('category').exclude(state=0)
            return qs
        else:
            profile = CustomUser.objects.get(user=self.request.user)
        if profile.moderator or profile.goverment or profile.user.is_superuser:
            qs = BlogPost.objects.select_related('owner', 'owner__user').prefetch_related('category')
        else:
            qs = BlogPost.objects.select_related('owner', 'owner__user').prefetch_related('category').exclude(state=0)
        return qs

    def get_context_data(self, **kwargs):
        context = super(BlogPostListView, self).get_context_data(**kwargs)
        return context


class BlogPostListViewTag(BlogPostListView):

    def get_queryset(self, **kwargs):
        category = self.kwargs['category_id']
        return super(BlogPostListViewTag, self).get_queryset().filter(category=category)


class BlogPostArhiveListView(ListView):
    model = BlogPost
    context_object_name = 'blog_posts'

    template_name = 'force_blog/arhive_news.html'

    paginate_by = 50

    def get_queryset(self):
        qs = BlogPost.objects.select_related('owner', 'owner__user').prefetch_related(
            'category').exclude(state=0)
        return qs


def blog_detail(request, pk):
    blogpost = BlogPost.objects.get(id=pk)

    if blogpost.state == DISABLE:
        try:
            profile = CustomUser.objects.get(user=request.user)
            if blogpost.owner.user == profile or profile.moderator or profile.goverment or profile.user.is_superuser:
                data = {'blogpost': blogpost, }
                return render_to_response('force_blog/blogpost_detail.html',
                                          data,
                                          context_instance=RequestContext(request))
            else:
                return redirect('/')
        except:
            return redirect('/')

    else:
        data = {'blogpost': blogpost, }
        return render_to_response('force_blog/blogpost_detail.html',
                                  data,
                                  context_instance=RequestContext(request))


@login_required
def blog_edit(request, blog_id):
    profile = CustomUser.objects.get(user=request.user)
    categorys = Category.objects.all()

    if not profile.moderator and profile.goverment and profile.user.is_superuser:
        return redirect('/login/')

    blog = BlogPost.objects.get(id=blog_id)

    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=blog)
        form.is_valid()
        try:
            tags = form.cleaned_data['category']
        except KeyError:
            new_tag = Category.objects.create(category=request.POST['category'])
        
        if form.is_valid():
            for x in categorys:
                blog.category.remove(x)

            for x in tags:
                try:
                    tag = Category.objects.get(category=x)
                except ObjectDoesNotExist:
                    pass
                
                try:
                    blog.category.add(tag)
                except TypeError:
                    pass

            form.save()
            url = u'/blog/%s' % blog_id
            return redirect(url)

    else:
        form = BlogPostForm(instance=blog)

    data = {'form': form, 'blog': blog, 'categorys': categorys}
    return render_to_response('force_blog/blogpost_edit.html',
                              data,
                              context_instance=RequestContext(request))


@login_required
def blog_new(request):
    profile = CustomUser.objects.get(user=request.user)
    categorys = Category.objects.all()
    form = BlogPostForm()

    if not profile.moderator and profile.goverment and profile.user.is_superuser:
        return redirect('/login/')

    if request.method == "POST":
        form = BlogPostForm(request.POST)
        form.is_valid()
        if form.is_valid():

            try:
                tags = form.cleaned_data['category']
            except KeyError:
                new_tag = Category.objects.create(category=request.POST['category'])

            # tags = form.cleaned_data['category']
            form.save_with_owner(owner=profile)
            blog = BlogPost.objects.first()
            for x in tags:
                tag = Category.objects.get(category=x)
                blog.category.add(tag)

            url = u'/blog/%s' % blog.id
            return redirect(url)

    data = {'form': form, 'categorys': categorys}
    return render_to_response('force_blog/blogpost_new.html',
                              data,
                              context_instance=RequestContext(request))


def blog_backup(blog, user):
    # blog_backup = blog
    # blog_backup.title = blog.title + ', user: ' + str(user.user) + ', date' + time.ctime()
    # blog_backup.state = 0
    # blog_backup.save()
    blog_edit = BlogEdit(user_edit=user)
    blog_edit.save()


@login_required
def blog_hidden(request, action, blog_id):
    profile = CustomUser.objects.get(user=request.user)

    if not profile.moderator and profile.goverment and profile.user.is_superuser:
        return redirect('/login/')
    else:
        blog = BlogPost.objects.get(id=int(blog_id))
        if action == "hide":
            blog.state = BlogPost.DISABLE
        elif action == "show":
            blog.state = BlogPost.ENABLE
        else:
            pass

        blog.save()
        return redirect(blog.get_absolute_url())
