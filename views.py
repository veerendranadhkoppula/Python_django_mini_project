from django.shortcuts import render

# Create your views here.

def feesCollection(request):
    return render(request,'finance/fees-collection.html')

def feesDueesReport(request):
    return render(request,'finance/due-report.html')

def feesCollectionReport(request):
    return render(request,'finance/collection-report.html')
