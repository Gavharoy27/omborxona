from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *
from datetime import *


class BolimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "bo'limlar.html")
        return redirect('login')


class MijozlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            mijozlar = Mijoz.objects.filter(bolim=request.user.sotuvchi.bolim)
            context = {
                'mijozlar': mijozlar
            }
            return render(request, "mijozlar.html", context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Mijoz.objects.create(
                ism=request.POST.get('ism'),
                dokon=request.POST.get('dokon'),
                tel=request.POST.get('tel'),
                manzil= None if request.POST.get('manzil') == '' else request.POST.get('manzil'),
                qarz=request.POST.get('qarz'),
                bolim=request.user.sotuvchi.bolim
            )
            return redirect('mijozlar')
        return redirect('login')


class MahsulotlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            mahsulotlar = Mahsulot.objects.filter(bolim=request.user.sotuvchi.bolim)
            context = {
                'mahsulotlar': mahsulotlar
            }
            return render(request, "mahsulotlar.html", context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Mahsulot.objects.create(
                nom=request.POST.get('nom'),
                brend=request.POST.get('brend'),
                narx1=request.POST.get('narx1'),
                narx2=None if request.POST.get('narx2') == "" else request.POST.get('narx2'),
                miqdor=request.POST.get('miqdor'),
                olchov=request.POST.get('olchov'),
                oxirgi_sana=datetime.now() if request.POST.get('sana') == "" else request.POST.get('sana'),
                bolim=request.user.sotuvchi.bolim
            )
            return redirect('mahsulotlar')
        return redirect('login')


class MahsulotTahrirlshView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mahsulotlar = Mahsulot.objects.filter(id=pk)
            context = {
                'mahsulotlar': mahsulotlar
            }
            return render(request, "mahsulot-tahrirlash.html", context)
        return redirect('login')

    def post(self, request, **kwargs):
        if request.user.is_authenticated:
            pk = kwargs.get('pk')
            mahsulot = get_object_or_404(Mahsulot, id=pk)

            mahsulot.nom = request.POST.get('nom')
            mahsulot.brend = request.POST.get('brend')
            mahsulot.narx1 = request.POST.get('narx1')
            mahsulot.narx2 = None if request.POST.get('narx2') == "" else request.POST.get('narx2')
            mahsulot.miqdor = request.POST.get('miqdor')
            mahsulot.olchov = request.POST.get('olchov')
            mahsulot.oxirgi_sana=datetime.now() if request.POST.get('sana') == "" else request.POST.get('sana')
            mahsulot.save()
            return redirect('mahsulotlar')
        return redirect('login')


class MijozTahrirlashView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mijozlar = Mijoz.objects.filter(id=pk)
            context = {
                'mijozlar':mijozlar
            }
            return render(request, "mijoz-tahrirlash.html", context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            mijoz = get_object_or_404(Mijoz, id=pk)

            mijoz.ism=request.POST.get('ism')
            mijoz.tel=request.POST.get('tel')
            mijoz.manzil=request.POST.get('manzil')
            mijoz.dokon=request.POST.get('dokon')
            mijoz.qarz=request.POST.get('qarz')
            mijoz.save()
            return redirect('mijozlar')
        return redirect('login')


def mahsulot_dc_view(request, pk):
    if request.user.is_authenticated:
        mahsulot = Mahsulot.objects.get(id=pk)
        context = {
            'mahsulot': mahsulot
        }
        return render(request, 'mahsulot_dc.html', context)
    return redirect('login')


def mijoz_dc_view(request, pk):
    if request.user.is_authenticated:
        mijoz = Mijoz.objects.get(id=pk)
        context = {
            'mijoz': mijoz
        }
        return render(request, 'mijoz_dc.html', context)
    return redirect('login')


def mahsulot_delete_view(request, pk):
    if request.user.is_authenticated:
        mahsulot = Mahsulot.objects.get(id=pk)
        mahsulot.delete()
        return redirect('mahsulotlar')
    return redirect('login')


def mijoz_delete_view(request, pk):
    if request.user.is_authenticated:
        mijoz = Mijoz.objects.get(id=pk)
        mijoz.delete()
        return redirect('mijozlar')
    return redirect('login')


