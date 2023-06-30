from django.shortcuts import render, get_object_or_404, redirect
from .models import Link
from .forms import LinkForm

def link_create(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('link_list')
    else:
        form = LinkForm()
    return render(request, 'links/link_create.html', {'form': form})

def link_update(request, pk):
    link = get_object_or_404(Link, pk=pk)
    if request.method == 'POST':
        form = LinkForm(request.POST, instance=link)
        if form.is_valid():
            form.save()
            return redirect('link_list')
    else:
        form = LinkForm(instance=link)
    return render(request, 'links/link_update.html', {'form': form, 'link': link})

def link_delete(request, pk):
    link = get_object_or_404(Link, pk=pk)
    if request.method == 'POST':
        link.delete()
        return redirect('link_list')
    return render(request, 'links/link_delete.html', {'link': link})

def link_list(request):
    links = Link.objects.all()
    return render(request, 'links/link_list.html', {'links': links})
    