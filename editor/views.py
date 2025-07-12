from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.timezone import localtime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Document, DocumentVersion
from django.contrib import messages
from .utils import check_grammar
import requests


@login_required
def dashboard(request):
    documents = Document.objects.filter(owner=request.user)
    return render(request, 'dashboard.html', {'documents': documents})

def create_document(request):
    if request.method == 'POST':
        title = request.POST['title']
        print("Creating document with title:", title)
        doc = Document.objects.create(title=title, owner=request.user)
        return redirect('editor', doc_id=doc.id)
    return render(request, 'create_document.html')

@login_required
def editor_view(request, doc_id):
    document = get_object_or_404(Document, id=doc_id, owner=request.user)

    if request.method == 'POST':
        new_title = request.POST.get('title', '').strip()
        new_content = request.POST.get('content', '').strip()

        # DEBUG PRINT
        print("Title from POST:", new_title)

        if new_title:
            document.title = new_title
        document.content = new_content
        document.save()

        messages.success(request, "Document updated successfully.")
        return redirect('editor', doc_id=doc_id)

    return render(request, 'editor.html', {'document': document})

@login_required
def delete_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id, owner=request.user)

    if request.method == 'POST':
        document.delete()
        messages.success(request, 'Document deleted successfully.')
        return redirect('dashboard')

    return redirect('editor', doc_id=doc_id)

@login_required
def ai_suggestions(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        suggestions = check_grammar(content)
        return JsonResponse({'suggestions': suggestions})