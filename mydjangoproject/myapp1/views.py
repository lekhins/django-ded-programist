from django.shortcuts import render
from myapp1.models import Worker


def index_page(request):
    all_workers = Worker.objects.all()
    print(all_workers)

    workers_filtered = Worker.object.filter(salary=180000)
    print(workers_filtered)

    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')
