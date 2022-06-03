from django.contrib import admin
from library import models

# Register your models here.

# 作者
class AuthorAdmin(admin.ModelAdmin):
    # 列出表格的字段
    list_display = ['authorid', 'authorname', 'authorage', 'authorcity', 'authortelno',
                    'authoremail', 'authorworkaddress']

# 图书类别
class BookTypeAdmin(admin.ModelAdmin):
    # 列出表格的字段
    list_display = ['id', 'typename']

# 出版社
class PressAdmin(admin.ModelAdmin):
    # 列出表格的字段
    list_display = ['pressid', 'pressname', 'presscity','presstelno', 'pressemail',
                     'pressaddress']


# 图书
class BookAdmin(admin.ModelAdmin):
    # 列出表格的字段
    list_display = ['bookid', 'bookname', 'booktype','bookauthor', 'bookprice',
                     'bookpress','booksumno']
    # 分页 -- 指定每页显示多少数据
    list_per_page = 10
    # Action的位置
    actions_on_top = True
    actions_on_bottom = True
    # 筛选 --filter
    list_filter = ['booktype','bookauthor']
    # 查询
    search_fields = ['bookid', 'bookname']




admin.site.register(models.Author, AuthorAdmin) # 作者表
admin.site.register(models.Booktype, BookTypeAdmin) # 图书类别
admin.site.register(models.Press,PressAdmin)  # 出版社
admin.site.register(models.Book,BookAdmin) # 图书
admin.site.register(models.Student) # 学生
admin.site.register(models.Borrowbook) # 借书表