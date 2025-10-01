from django.shortcuts import render
from django.http import JsonResponse
from .models import DateTimeRecord
from datetime import datetime

def index(request):
    """Render the main page"""
    return render(request, 'index.html')

def get_datetime(request):
    """Retrieve all datetime records from database"""
    if request.method == 'GET':
        records = DateTimeRecord.objects.all().values('id', 'recorded_date', 'recorded_time', 'created_at')
        data = list(records)
        return JsonResponse({'records': data}, safe=False)

def add_datetime(request):
    """Add current datetime to database"""
    if request.method == 'POST':
        now = datetime.now()
        record = DateTimeRecord.objects.create(
            recorded_date=now.date(),
            recorded_time=now.time()
        )
        return JsonResponse({
            'success': True,
            'id': record.id,
            'date': str(record.recorded_date),
            'time': str(record.recorded_time)
        })