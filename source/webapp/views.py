from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.utils.timezone import make_naive

from webapp.models import GuestBook
from webapp.forms import GuestBookForm


def index_view(request):
    data = GuestBook.objects.filter(status='active').order_by('-created_at')
    return render(request, 'index.html', context={
        'guest_books': data
    })


def guest_book_view(request, pk):
    guest_book = get_object_or_404(GuestBook, pk=pk)
    context = {'guest_book': guest_book}
    return render(request, 'guest_book_view.html', context)


def guest_book_create_view(request):
    if request.method == "GET":
        return render(request, 'guest_book_create.html', context={
            'form': GuestBookForm()
        })
    elif request.method == 'POST':
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            # guest_book = Product.objects.create(**form.cleaned_data)
            guest_book = GuestBook.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],
                status=form.cleaned_data['status']
            )
            return redirect('index')
        else:
            return render(request, 'guest_book_create.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

#
# def guest_book_update_view(request, pk):
#     guest_book = get_object_or_404(GuestBook, pk=pk)
#     if request.method == "GET":
#         form = GuestBookForm(initial={
#             'name': guest_book.name,
#             'description': guest_book.description,
#             'category': guest_book.category,
#             'amount': guest_book.amount,
#             'price': guest_book.price,
#         })
#         return render(request, 'guest_book_update.html', context={
#             'form': form,
#             'guest_book': guest_book
#         })
#     elif request.method == 'POST':
#         form = GuestBookForm(data=request.POST)
#         if form.is_valid():
#             # guest_book.objects.filter(pk=pk).update(**form.cleaned_data)
#             guest_book.name = form.cleaned_data['name']
#             guest_book.description = form.cleaned_data['description']
#             guest_book.category = form.cleaned_data['category']
#             guest_book.amount = form.cleaned_data['amount']
#             guest_book.price = form.cleaned_data['price']
#             guest_book.save()
#             return redirect('guest_book_view', pk=guest_book.pk)
#         else:
#             return render(request, 'guest_book_update.html', context={
#                 'guest_book': guest_book,
#                 'form': form
#             })
#     else:
#         return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
#
#
# def guest_book_delete_view(request, pk):
#     guest_book = get_object_or_404(GuestBook, pk=pk)
#     if request.method == 'GET':
#         return render(request, 'guest_book_delete.html', context={'guest_book': guest_book})
#     elif request.method == 'POST':
#         guest_book.delete()
#         return redirect('index')
#     else:
#         return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
