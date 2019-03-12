from django.shortcuts import render, redirect, get_object_or_404
from category.models import Category

def index(request):
    expenditure = Category.objects.filter(cat_type = 1)
    income = Category.objects.filter(cat_type = 0)
    context = {
        'expenditure' : expenditure,
        'income' : income
    }
    return render(request, 'category/index.html', context)

def add_category(request):
    if request.method == 'POST':
        name = request.POST['name']
        cat_type = request.POST['cat_type']
        icon = request.FILES['icon']
        category = Category(name = name, cat_type = cat_type, icon = icon)
        if category:
           category.save()
           return redirect('category')
    return render(request, 'category/add-category.html')

def edit_category_form(request, cat_id):
    category = Category.objects.get(pk = cat_id)
    context = {
        'category' : category
    }
    return render(request, 'category/edit-category.html', context)

def edit_category_save(request):
    if request.method == 'POST':
        name = request.POST['name']
        cat_type = request.POST['cat_type']
        icon = request.FILES['icon']
        categoryid = request.POST['categoryid']

        category = Category.objects.get(pk = categoryid)
        category.name = name
        category.cat_type = cat_type
        category.icon = icon
        category.save()

    return redirect('category')
    
def delete_category(request, cat_id):
    delete = get_object_or_404(Category, pk=cat_id)
    delete.delete() 
    return redirect('category')
