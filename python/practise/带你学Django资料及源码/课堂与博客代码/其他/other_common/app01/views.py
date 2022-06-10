from django.shortcuts import render
from .models import Area
from django.http import JsonResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def get_parent(request):
    print('视图执行了')
    # print(1 / 0)
    areas = Area.objects.filter(parent__isnull=True).all()
    l = []
    for area in areas:
        temp = {}
        temp['id'] = area.id
        temp['name'] = area.name
        temp['parent'] = area.parent
        l.append(temp)

    return JsonResponse({"data": l})


# 山西省--->市
def get_area(request, id):
    print(id)
    areas = Area.objects.filter(parent=id).all()

    l = []
    for area in areas:
        temp = {}
        temp['id'] = area.id
        temp['name'] = area.name
        temp['parent'] = str(area.parent)
        l.append(temp)

    return JsonResponse({"data": l}, safe=False)
