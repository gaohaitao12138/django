from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Position
from django.db.models import CharField, Value
from django.db.models.functions import Concat
from django.http import JsonResponse
from django.http import JsonResponse
from django.db.models import Q
from django.template.loader import render_to_string

def login(request):
    return render()

def index(request):
    if request.method == 'POST':
        city_position = request.POST['query']
        print(city_position)
        print('1')
        return


    return render(request,'index2.html')


def custom(request):
    return render(request,'custom.html')



def cs(request):
    return render(request,'cs.html')

def demo(request):
    return render(request,'demo.html')

from django.shortcuts import render
from .models import QuestionCategory, Question, Answer

# def qa(request):
#     return render(request,'QA.html')


from django.shortcuts import render
from .models import Person

from django.db.models import Q

def qa(request):
    categories = QuestionCategory.objects.all()
    context = {
        'categories': categories
    }
    print(categories)
    return render(request, 'QA.html', context)
def person_list(request):
    persons = Person.objects.all()  # 这里应该是 Position.objects.all()，因为你在展示的是岗位信息
    print(persons)
    # 获取所有不重复的职能类型和工作地点
    unique_job_types = Position.objects.values_list('job_type', flat=True).distinct()
    unique_work_locations = Position.objects.values_list('work_location', flat=True).distinct()
    # 为每个列表添加“全部”选项
    job_types = ['全部'] + list(unique_job_types)
    work_locations = ['全部'] + list(unique_work_locations)
    # 将数据传递给模板
    context = {
        'persons': persons,
        'job_types': job_types,
        'work_locations': work_locations,
    }
    return render(request, "models.html", context)





def position(request):
    # 获取查询参数
    job_type = request.GET.get('job_type', '全部')
    work_location = request.GET.get('work_location', '全部')
    search_query = request.GET.get('search', '')

    # 构建查询集
    positions = Position.objects.all()
    if job_type != '全部':
        positions = positions.filter(job_type=job_type)
    if work_location != '全部':
        positions = positions.filter(work_location=work_location)
    if search_query:
        positions = positions.filter(
            Q(name__icontains=search_query) |
            Q(job_type__icontains=search_query) |
            Q(work_location__icontains=search_query) |
            Q(responsibility__icontains=search_query) |
            Q(requirement__icontains=search_query)
        )

        # 获取所有唯一的职位类型和工作地点（这部分逻辑可以保持不变）
    unique_job_types = Position.objects.values_list('job_type', flat=True).distinct().order_by('job_type')
    job_types = ['全部'] + list(unique_job_types)
    unique_work_locations = Position.objects.values_list('work_location', flat=True).distinct().order_by(
        'work_location')
    work_locations = ['全部'] + list(unique_work_locations)

    # 将这些列表传递给模板
    context = {
        'positions': positions,
        'job_types': job_types,
        'work_locations': work_locations,
    }
    return render(request, 'position.html', context)


def filter_positions(request):
    job_type = request.GET.get('job_type')
    work_location = request.GET.get('work_location')
    search_term = request.GET.get('search_term')

    positions = Position.objects.all()

    # 应用job_type和work_location过滤条件（如果提供了的话）
    if job_type and job_type != '全部':
        positions = positions.filter(job_type=job_type)
    if work_location and work_location != '全部':
        positions = positions.filter(work_location=work_location)

        # 应用搜索框的过滤条件（如果提供了的话）
    if search_term:
        positions = positions.filter(
            Q(name__icontains=search_term) |
            Q(job_type__icontains=search_term) |  # 添加对类型的搜索
            Q(work_location__icontains=search_term) |  # 添加对地址的搜索
            Q(responsibility__icontains=search_term) |
            Q(requirement__icontains=search_term)
        )

    html_content = render_to_string('partial_position_list.html', {'positions': positions})
    return JsonResponse({'html_content': html_content})


