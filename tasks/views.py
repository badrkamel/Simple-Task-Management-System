import csv
import xlwt
from xlwt import Workbook 
from .permissions import IsOwner
from rest_framework import viewsets, status
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
        
from rest_framework.permissions import IsAuthenticated


class TaskView(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


@api_view(['GET'])
def my_tasks(request):
    """
    List my all tasks.
    """
    tasks = Task.objects.filter(user=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    """
    Get a specific task
    """
    try:
        task = Task.objects.get(user=request.user, pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task)
    return Response(serializer.data)



@api_view(['GET'])
def tasks_completed(request):
    """
    List my all completed tasks.
    """
    tasks = Task.objects.filter(
        user=request.user,
        completed=True
    )
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def tasks_incompleted(request):
    """
    List all incompleted tasks.
    """
    tasks = Task.objects.filter(
        user=request.user, 
        completed=False
    )
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)



def save_as_csv(request):
    """
        Export data to csv file.
    """
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tasks_rate.csv"'

    # Retrieve the username of the data owner.
    user_name = request.user.username

    # Number of completed tasks
    completed_tasks = Task.objects.filter(
        user=request.user, completed=True).count()

    # Number of incompleted tasks
    incompleted_tasks = Task.objects.filter(
        user=request.user, completed=False).count()

    # Number of all tasks
    all_tasks = Task.objects.filter(user=request.user).count()

    # Calculate the ratio between completed and incomplete tasks.
    rate = 100
    if incompleted_tasks != 0:
        rate = round((completed_tasks*100)/(all_tasks), 1)


    writer = csv.writer(response)

    # f-Strings: A New and Improved Way to Format Strings in Python>= 3.6
    writer.writerow(['Username', f'{user_name}'])
    writer.writerow([])
    writer.writerow(['All Tasks', 'Completed', 'Incompleted', 'Rate'])
    writer.writerow([f'{all_tasks}', f'{completed_tasks}', f'{incompleted_tasks}', f'%{rate}'])


    return response



def save_as_xls(request):
    """
        Export data to excel file.
    """

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="tasks_rate.xls"'

    # Workbook is created 
    wb = Workbook() 

    # add_sheet is used to create sheet. 
    sheet1 = wb.add_sheet('Ratio') 

    name_style = xlwt.easyxf('font: bold 1, color red')
    style = xlwt.easyxf('font: bold 1')

    user_name = request.user.username

    sheet1.write(0, 0, 'Username', name_style) 
    sheet1.write(0, 1, f'{user_name}', name_style)

    # Heads
    sheet1.write(2, 0, 'All Tasks', style)
    sheet1.write(2, 1, 'Completed', style)
    sheet1.write(2, 2, 'Incompleted', style)
    sheet1.write(2, 3, 'Rate', style)

    completed_tasks = Task.objects.filter(
        user=request.user, completed=True).count()

    incompleted_tasks = Task.objects.filter(
        user=request.user, completed=False).count()

    all_tasks = Task.objects.filter(user=request.user).count()

    rate = 100
    if incompleted_tasks != 0:
        rate = round((completed_tasks*100)/(all_tasks), 1)

    sheet1.write(3, 0, f'{all_tasks}')
    sheet1.write(3, 1, f'{completed_tasks}')
    sheet1.write(3, 2, f'{incompleted_tasks}')
    sheet1.write(3, 3, f'%{rate}')

    # save the file.
    wb.save(response)

    return response