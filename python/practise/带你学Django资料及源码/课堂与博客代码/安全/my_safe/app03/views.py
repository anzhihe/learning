from django.shortcuts import render

# Create your views here.
from django.db import connection


def index(request):
    # id = request.GET.get('id')

    # sql = 'select id,name from app03_user where id=%s' % (id)

    '''
    select id,name from app03_user where id=1

    select id,name from app03_user where id=1 or 1=1

    '''
    name = request.GET.get('name')
    sql = "select id,name from app03_user where name='%s' " % (name)


    '''
    select id,name from app03_user where name='laosong'  
    
    
    
    
    select id,name from app03_user where name='laosong' or '1=2'
    
    '''
    cursor = connection.cursor()
    cursor.execute(sql)

    sql = "select id,name from app03_user where name=%s"
    # cursor.execute(sql,(name,))
    rows = cursor.fetchall()

    ctx = {
        'rows': rows
    }
    return render(request, 'app03/index.html', ctx)
