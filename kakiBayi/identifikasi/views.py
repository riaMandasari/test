from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request,"index.html")


def pelatihan(request):
    context = {
        'heading' : 'Pelatihan'
    } 
    
    if request.method == 'POST':
        context['nama_model'] = request.POST['nama_model']
        context['num_epoch'] = request.POST['num_epoch']
    
    

    return render(request,'pelatihan.html', context)


def pengujian(request):
    return render(request,'pengujian.html')