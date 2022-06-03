from django.shortcuts import render,reverse,redirect
from . import models
from django.http import HttpResponse
# 导入用于分页的模块
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
from django.conf import settings

# Create your views here.
# 定义一个字段，选中哪些值
ACTIVE_ITEM = {
    'type': ('', "全部"),
    'price': ('', '全部'),
    'difficult': ('', '全部'),
    'author': ('', '全部'),
    'keyword': '',
    'order': 0,  # 0--忽略排序 ，1--降序  2--升序
}
SELECT_ITEM = {
    'type': ['全部'],
    'price': ['全部', '0-20元', '20-30元', '30-40元', '40-50元', '50-60元', '60-70元', '70-80元', '80元以上'],
    'difficult': ['全部', '入门', '中级', '高级'],
    'author': ['全部'],
}
TIPS = [
        ("凤凰自营", "有凤凰传媒自己出版和经营的图书"),
        ("热销图书", "本周销售前100名的图书"),
        ("满99减20", "所有标注满99减20商品才销售满减"),
        ("限时抢", "在每天中午12:00有优惠"),
        ('提供电子书', "购买图书即送对应的电子书"),
]

def get_select_item():
    """
    获取查询的条目
    :return: 
    """
    # 读取Booktype填充
    if len(SELECT_ITEM['type']) == 1:
        booktypes = models.Booktype.objects.all().values('typename')
        for booktype in booktypes:
            SELECT_ITEM['type'].append(booktype['typename'])

    if len(SELECT_ITEM['author']) == 1:
        authors = models.Author.objects.all().values('authorname')
        for author in authors:
            SELECT_ITEM['author'].append(author['authorname'])
    # 遍历

def index(request):

    # 加载查询条目明细
    get_select_item()

    # 准备图书信息
    books = models.Book.objects.all().values()  # 所有图书！

    # 思路: 先判断 --》类型 --》价格 ---》 作者  ---》过滤关键字 ----》排序 ---》 最后结果！！！
    # === 筛选图书类别====
    if ACTIVE_ITEM['type'][0] != "":
        books = books.filter(booktype__exact = ACTIVE_ITEM['type'][0]).values()
    # === 筛选图书价格 ====
    if ACTIVE_ITEM['price'][0] != "":
        books = books.filter(bookprice__range =(ACTIVE_ITEM['price'][0], ACTIVE_ITEM['price'][2])).values()
    # === 筛选图书作者 ====
    if ACTIVE_ITEM['author'][0] != "":
        books = books.filter(bookauthor__exact = ACTIVE_ITEM['author'][0]).values()
    # === 过滤关键字 ====
    books = books.filter(bookname__contains=ACTIVE_ITEM['keyword']).values()
    # === 排序 ====
    if ACTIVE_ITEM['order'] == 1:
        books = books.order_by('-bookprice').values()
    elif ACTIVE_ITEM['order'] == 2:
        books = books.order_by('bookprice').values()

    #  ======= 实现分页 =============
    # 实例化一个分页的对象
    paginater = Paginator(books, settings.PRE_PAGE_NUMBER)
    # 得到当前数据的页数
    page = request.GET.get('page')
    # 获取每页的数据
    try:
        current_page_books = paginater.page(page)
    except PageNotAnInteger:
        current_page_books = paginater.page(1)
    except EmptyPage:
        current_page_books = paginater.page(paginater.num_pages)

    # 遍历
    for book in current_page_books:
        # 添加图片
        book['img'] = '../static/img/icon/' + str(book['bookid']) + '.jpg'
        # 查询作者的信息
        author = models.Author.objects.filter(authorid=book['bookauthor_id']).values()
        # 附加到结果集中
        book['author'] = author[0]['authorname']
        # 获得一个Tips
        tip = TIPS[random.randint(0, len(TIPS)-1)]
        # 添加到图书中
        book['tip'] = tip

    # 加载页面
    return render(request, 'index.html', context={'select_item': SELECT_ITEM,
                                                  'active': ACTIVE_ITEM,
                                                  'books': current_page_books,
                                                   })

def select_click(request):
    # 传值过来
    type = request.GET.get('type')
    name = request.GET.get('name')
    # 输出
    print("类别：%s \t 名称：%s" %(type, name))
    # 根据中文名称来判断修改！
    if '类别' in type:
        if name == '全部':
            ACTIVE_ITEM['type'] = ("", "全部")
        else:
            type_obj = models.Booktype.objects.filter(typename=name).values()  # Queryset [obj, obj, obj]
            ACTIVE_ITEM['type'] = (type_obj[0]['id'], type_obj[0]['typename'])

    elif '价格' in type:
        if name == '全部':
            ACTIVE_ITEM['price'] = ("", "全部")
        else:
            if '0-20' in name:
                ACTIVE_ITEM['price'] = (0, name, 20)
            elif '20-30' in name:
                ACTIVE_ITEM['price'] = (20, name,  30)
            elif '30-40' in name:
                ACTIVE_ITEM['price'] = (30, name,  40)
            elif '40-50' in name:
                ACTIVE_ITEM['price'] = (40, name, 50)
            elif '50-60' in name:
                ACTIVE_ITEM['price'] = (50, name, 60)
            elif '60-70' in name:
                ACTIVE_ITEM['price'] = (60, name, 70)
            elif '70-80' in name:
                ACTIVE_ITEM['price'] = (70, name, 80)
            elif '80元以上' in name:
                ACTIVE_ITEM['price'] = (80, name, 100000)

    elif '难度' in type:
        if name == '入门': ACTIVE_ITEM['difficult'] = (1, '入门')
        elif name == '中级': ACTIVE_ITEM['difficult'] = (2, '中级')
        elif name == '高级': ACTIVE_ITEM['difficult'] = (3, '高级')
    elif '作者' in type:
        if name == "全部":
            ACTIVE_ITEM['author'] = ('', '全部')
        else:
            author_obj = models.Author.objects.filter(authorname=name).values()
            ACTIVE_ITEM['author'] = (author_obj[0]['authorid'], author_obj[0]['authorname'])

    # 跳转
    return redirect(reverse('index'))

def get_keyword(request):
    # 获取keyword值
    keyword = request.GET.get('keyword')
    # 赋值
    ACTIVE_ITEM['keyword'] = keyword
    # 跳转
    return redirect(reverse('index'))

def get_all_book(request):
    # 清楚所有条件
    ACTIVE_ITEM['type'] = ('', '全部')
    ACTIVE_ITEM['price'] = ('', '全部')
    ACTIVE_ITEM['difficult'] = ('', '全部')
    ACTIVE_ITEM['author'] = ('', '全部')
    ACTIVE_ITEM['keyword'] = ""
    # 跳转
    return redirect(reverse('index'))

def get_order_number(request):
    # 获取Tag值
    tag = request.GET.get('tag')
    # 赋值
    ACTIVE_ITEM['order'] = int(tag)
    # 跳转到首页
    return redirect(reverse('index'))