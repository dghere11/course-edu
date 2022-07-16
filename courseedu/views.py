from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from courseedu.siteadmin.models import coursecategories

def index(request):
    categories=coursecategories.objects.filter(is_visible=True)
    categoriesData={
        'categories':categories
    }
    return render(request,'index.html',categoriesData)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

@login_required
def siteadminView(request):
    entries=coursecategories.objects.all()
    table={'entries':entries}
    i=coursecategories.objects.count()
    if i>0:
        latest=coursecategories.objects.latest('sno').sno
        if latest > i:
            j=1
            for entry in entries:
                if entry.sno!=j:
                    entry.sno=j
                    j+=1
                    entry.save()
                else:
                    j+=1
    return render(request,'accounts/siteadmin.html',table)

@login_required
def addcategory(request):
    if request.method=='POST':
        if coursecategories.objects.count()==0:
            sno=1
        else:
            sno=coursecategories.objects.latest('sno').sno+1
        name=request.POST.get('name')
        short_name=request.POST.get('short_name')
        content_id=request.POST.get('content_id')
        description=request.POST.get('description')
        img=request.FILES.get('img')
        if request.POST.get('is_visible')=="True":
            is_visible=True
        else:
            is_visible=False
        new_category=coursecategories(sno=sno,name=name,short_name=short_name,content_id=content_id,description=description,img=img,is_visible=is_visible)
        new_category.save()
        messages.success(request, 'Data has been entered!')
    return render(request,'accounts/addcategory.html',{})

@login_required
def viewcategory(request,id):
    entry=coursecategories.objects.get(pk=id)
    data={
        'Name':entry.name,
        'Short Name':entry.short_name,
        'Content id':entry.content_id,
        'Description':entry.description,
        'Image':entry.img,
        'Homepage Visibility':entry.is_visible
    }
    return render(request,'accounts/viewentry.html',{'data':data})

@login_required
def editcategory(request, id):
    entry=coursecategories.objects.get(pk=id)
    data={
        'Category Name':(entry.name,'Category Name'),
        'Short Name':(entry.short_name,'Short Name'),
        'Content id':(entry.content_id,'XXXX'),
        'Description':(entry.description,'Describe the course category.'),
        'Image':(entry.img,'Image'),
        'Homepage Visibility':(entry.is_visible,'')
    }
    if request.method=='POST':
        entry.name=request.POST.get('Category Name')
        entry.short_name=request.POST.get('Short Name')
        entry.content_id=request.POST.get('Content id')
        entry.description=request.POST.get('Description')
        entry.img=request.FILES.get('img')
        if request.POST.get('is_visible')=="True":
            entry.is_visible=True
        else:
            entry.is_visible=False
        entry.save()
        messages.success(request, 'Data has been updated!')
    return render(request,'accounts/editentry.html',{'data':data})

@login_required
def deletecategory(request,id):
    entry=coursecategories.objects.get(pk=id)
    entry.delete()
    return redirect('siteadmin')

@login_required
def showentry(request):
    entries=coursecategories.objects.filter(selection=True)
    for entry in entries:
        entry.is_visible=True
        entry.save()
    if len(entries)>0:
        messages.success(request, 'Selected entries will be shown at homepage')
    return redirect('siteadmin')

@login_required
def hideentry(request):
    entries=coursecategories.objects.filter(selection=True)
    for entry in entries:
        entry.is_visible=False
        entry.save()
    if len(entries)>0:
        messages.success(request, 'Selected entries will be hidden at homepage')
    return redirect('siteadmin')

@login_required
def deleteselected(request):
    entries=coursecategories.objects.filter(selection=True)
    for entry in entries:
        entry.delete()
    return redirect('siteadmin')

@login_required
def selectallentry(request):
    entries=coursecategories.objects.all()
    for entry in entries:
        entry.selection=True
        entry.save()
    return redirect('siteadmin')

@login_required
def resetselection(request):
    entries=coursecategories.objects.all()
    for entry in entries:
        entry.selection=False
        entry.save()
    return redirect('siteadmin')

@login_required
def select(request,id):
    entry=coursecategories.objects.get(pk=id)
    entry.selection=True
    entry.save()
    return redirect('siteadmin')

@login_required
def deselect(request,id):
    entry=coursecategories.objects.get(pk=id)
    entry.selection=False
    entry.save()
    return redirect('siteadmin')