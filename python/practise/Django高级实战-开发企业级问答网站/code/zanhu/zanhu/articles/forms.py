#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from django import forms

from markdownx.fields import MarkdownxFormField

from zanhu.articles.models import Article


class ArticleForm(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())  # 隐藏
    edited = forms.BooleanField(widget=forms.HiddenInput(), required=False, initial=False)  # 隐藏
    content = MarkdownxFormField()

    class Meta:
        model = Article
        fields = ["title", "content", "image", "tags", "status", "edited"]
