from django.shortcuts import get_object_or_404, render

from .models import DataSet

def index(request):
    datasets = DataSet.objects.all()
    context = {
        'datasets': datasets
    }
    return render(request, 'datasets/index.html', context)

def detail(request, dataset_id):
    dataset = get_object_or_404(DataSet, id=dataset_id)
    context = {
        'dataset': dataset
    }
    return render(request, 'datasets/detail.html', context)