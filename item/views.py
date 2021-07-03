from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Item, ItemComment
from .forms import ItemForm, ItemCommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def homeitem(request):
    items = Item.objects.all()
    return render(request, 'homeitem.html', {'items_list': items})


def newitem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.user = item.author
            item.save()
            return redirect('homeitem')

    else:
        form = ItemForm()
    return render(request, 'newitem.html', {'form': form})


def detailitem(request, index):
    item = get_object_or_404(Item, pk=index)
    comment_list = ItemComment.objects.filter(item=item)
    if request.method == "POST":
        comment_form = ItemCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            # comment.author=request.user
            comment.published_date = timezone.now()
            # comment.user=request.user
            comment.item = item
            comment.save()
            return redirect('detailitem', index=index)
    else:
        comment_form = ItemCommentForm
    return render(request, 'detailitem.html', {'item': item, 'comment_list': comment_list, 'comment_form': comment_form})


def edititem(request, index):
    item = get_object_or_404(Item, pk=index)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.save()
            return redirect('detailitem', index=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'edititem.html', {'form': form})


def deleteitem(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('homeitem')


def delete_comment(request, index, comment_pk):
    comment = get_object_or_404(ItemComment, pk=comment_pk)
    comment.delete()
    return redirect('detailitem', index=index)

# @login_required
# def like_item(request, item_id):
#     item = get_object_or_404(Item, id=item_id)
#     if request.user in item.like_users.all():
#         item.like_users.remove(request.user)
#     else:
#         item.like_users.add(request.user)
