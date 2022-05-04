from django.shortcuts import render,  redirect
from .models import members
def member(request):
    member = members.objects.all()
    return render( request, 'spon/members.html', {'member':member})

def search(request):
    search = request.POST['searched']
    search_member = members.objects.filter(FullName__contains=search)
    if request.method == 'POST':
        return render(request, 'spon/searched.html', {'search':search_member})
    else:
         return render(request, 'spon/searched.html',{})

def populate(request):
    return render(request, 'spon/populate.html',{})

def login(request):
    return redirect("create_member")

def create_member(request):
    return render(request, 'spon/create_member.html',{})

def create_member_details(request):
    members.objects.create(
        FullName = request.POST['FullName'],
        Gender = request.POST['Gender'],
        SponNo = request.POST['SponNo'],
        PhoneNo = request.POST['PhoneNo'],
        State = request.POST['State'],
        LocalGov = request.POST['LocalGov'],
        Status = request.POST['Status']
    ) 
    return redirect('create_member')

def edit(request):
    mode = members.objects.all()
    return render(request, 'spon/edit.html',{'mode':mode})

def edit_member(request, id):
    value = members.objects.get(id=id)
    return render(request, 'spon/edit_member.html', {"detail":value})

def edit_member_detail(request, id):
    value = members.objects.get(id=id)
    value.FullName = request.POST['FullName']
    value.Gender = request.POST['Gender']
    value.SponNo = request.POST['SponNo']
    value.PhoneNo = request.POST['PhoneNo']
    value.State = request.POST['State']
    value.LocalGov = request.POST['LocalGov']
    value.Status = request.POST['Status']
    value.save()
    return redirect('edit')

def search_edit(request):
    search = request.POST['searched']
    search_member = members.objects.filter(FullName__contains=search)
    if request.method == 'POST':
        return render(request, 'spon/searched_edit.html', {'search':search_member})
    else:
         return render(request, 'spon/searched_edit.html',{})
