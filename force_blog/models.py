# coding=utf-8

from django.db import models
from django.conf import settings
from redactor.fields import RedactorField


class BlogPost(models.Model):
    DISABLE = 0
    ENABLE = 1
    HOT_POST = 2

    STATE_CHOICE = (
        (DISABLE, 'Новость отключена'),
        (ENABLE, 'Обычная Новость'),
        (HOT_POST, 'Важная Новость (На главной)'),
    )

    title = models.CharField(max_length=50, verbose_name=u'Заголовок')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_publication = models.DateTimeField(blank=True, null=True)

    owner = models.ForeignKey(settings.AUTH_PROFILE_MODULE,
                              verbose_name=u'Автор')
    text = RedactorField(verbose_name=u'Text', redactor_options={'plugins': ['table']})


    state = models.SmallIntegerField(default=ENABLE,
                                     choices=STATE_CHOICE,
                                     verbose_name=u'Статус')

    category = models.ManyToManyField('Category',
                                      verbose_name=u'Теги',
                                      related_name="blogposts_category")

    blog_edit = models.ManyToManyField('BlogEdit',
                                       blank=True, null=True,
                                       verbose_name=u'Редактирование',
                                       related_name="blogpost_edit")

    image = models.ImageField(upload_to='BlogImage/',
                              verbose_name=u'Изображение',
                              blank=True,
                              null=True)

    default_image = models.ForeignKey('DefaultImageBlog',
                                      verbose_name=u'Изображение',
                                      blank=True, null=True)

    if_comments = models.BooleanField(default=True)

    class Meta:
        ordering = ["-date_creation"]
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return u'/blog/%s' % self.id

    def __unicode__(self):
        return u'%s %s - %s' % (self.title,
                                self.owner,
                                self.state,)


class AttachedFiles(models.Model):
    file_name = models.CharField(max_length=50)
    one_file = models.FileField(upload_to='AttachedFiles/')
    category = models.ManyToManyField('Category',
                                      verbose_name=u'Категории',
                                      related_name="file_category")

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def get_absolute_url(self):
        return u'/files/%s' % self.id

    def __unicode__(self):
        return self.file_name


class Category(models.Model):
    category = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __unicode__(self):
        return self.category


class BlogEdit(models.Model):
    date_edit = models.DateTimeField(auto_now_add=True)
    user_edit = models.ForeignKey(settings.AUTH_PROFILE_MODULE,
                                  verbose_name=u'Автор')

    class Meta:
        verbose_name = 'Редактирование'
        verbose_name_plural = 'Редактирование'

    def __unicode__(self):
        return u'%s - %s' % (self.date_edit,
                             self.user_edit,)


class DefaultImageBlog(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='DefaultImageBlog/',
                              verbose_name=u'Изображение')

    class Meta:
        verbose_name = 'Изображение по умолчанию'
        verbose_name_plural = 'Изображения по умолчанию'

    def __unicode__(self):
        return self.name
