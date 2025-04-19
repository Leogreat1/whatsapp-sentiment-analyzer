from django.shortcuts import render
from .chat_parser import handle_uploaded_chat_file

def home(request):
    return render(request, 'analyzer/home.html')

def upload_chat(request):
    if request.method == 'POST' and request.FILES.get('chat_file'):
        file = request.FILES['chat_file']
        result = handle_uploaded_chat_file(file.read())
        return render(request, 'analyzer/result.html', {'messages': result})
    return render(request, 'analyzer/home.html', {'error': 'Please upload a file.'})
