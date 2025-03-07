from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *


def ogohlantirish_view(request):
    return render(request, "ogohlantirish.html")


class SotuvlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            sotuvlar = Sotuv.objects.filter(bolim=request.user.sotuvchi.bolim)
            mahsulotlar = Mahsulot.objects.order_by('nom')
            mijozlar = Mijoz.objects.order_by('ism')
            context = {
                'sotuvlar': sotuvlar,
                'mahsulotlar': mahsulotlar,
                'mijozlar': mijozlar,
            }
            return render(request, "sotuvlar.html", context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            qarz = None if request.POST.get('qarz') == "" else float(request.POST.get('qarz'))
            mijoz = Mijoz.objects.get(id=request.POST.get('mijoz_id'))

            mahsulot = Mahsulot.objects.get(id=request.POST.get('mahsulot_id'))
            miqdor = request.POST.get('miqdor')

            if float(miqdor) > mahsulot.miqdor:
                return render(request, "ogohlantirish.html", {"message": "Mahsulot yetarli emas!"})

            Sotuv.objects.create(
                mahsulot=mahsulot,
                mijoz=mijoz,
                jami_summa=request.POST.get('jami_summa'),
                miqdor=miqdor,
                tolandi=request.POST.get('tolandi'),
                qarz=qarz,
                bolim=Bolim.objects.first()
            )

            mijoz.qarz += qarz
            mijoz.save()

            mahsulot.miqdor -= miqdor
            mahsulot.save()
            return redirect('sotuvlar')
        return redirect('login')

class SotuvTahrirlashView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            sotuv = get_object_or_404(Sotuv, id=pk)
            mahsulotlar = Mahsulot.objects.all()
            mijozlar = Mijoz.objects.all()
            context = {
                'sotuv': sotuv,
                'mahsulotlar': mahsulotlar,
                'mijozlar': mijozlar,
            }
            return render(request, 'sotuv_tahrirlash.html', context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            sotuv = get_object_or_404(Sotuv, id=pk)

            mahsulot = get_object_or_404(Mahsulot, id=request.POST.get('mahsulot_id'))
            mijoz = get_object_or_404(Mijoz, id=request.POST.get('mijoz_id'))

            sotuv.mahsulot = mahsulot
            sotuv.mijoz = mijoz
            sotuv.jami_summa = float(request.POST.get('jami_summa', 0))
            sotuv.miqdor = float(request.POST.get('miqdor', 0))
            sotuv.tolandi = float(request.POST.get('tolandi', 0))
            sotuv.qarz = float(request.POST.get('qarz', 0))
            sotuv.bolim = request.user.sotuvchi.bolim

            sotuv.save()
            return redirect('sotuvlar')

        return redirect('login')


def sotuv_dc_view(request, pk):
    if request.user.is_authenticated:
        sotuv = Sotuv.objects.get(id=pk)
        context = {
            'sotuv': sotuv
        }
        return render(request, 'sotuv_dc.html', context)
    return redirect('login')


def sotuv_delete_view(request, pk):
    if request.user.is_authenticated:
        sotuv = Sotuv.objects.get(id=pk)
        sotuv.delete()
        return redirect('sotuvlar')
    return redirect('login')
