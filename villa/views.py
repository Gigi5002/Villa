from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .models import Villa
from .filters import VillaFilters
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .form import VillaUpdateForm


def index_view(request):
    villas = Villa.objects.filter(is_active=True)[:6]
    return render(request, 'villa/index.html', {'villas': villas})


class VillaListView(ListView):
    model = Villa
    template_name = 'villa/villa_list.html'
    context_object_name = 'villas'
    filterset_class = VillaFilters
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = VillaFilters(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filter'] = self.filterset

        villas = context['villas']
        pagination = Paginator(villas, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            villas = pagination.page(page)
        except PageNotAnInteger:
            villas = pagination.page(1)
        except EmptyPage:
            villas = pagination.page(pagination.num_pages)
        context['villas'] = villas

        return context


def villa_detail_view(request, pk):
    villa = Villa.objects.filter(id=pk).first()

    return render(request, 'villa/villa_detail.html', {'villa': villa})


@user_passes_test(lambda u: u.status == 2 or u.is_admin, login_url='/index/')
def villa_update_view(request, pk):
    villa = Villa.objects.filter(id=pk).first()

    if request.method == 'POST':
        form = VillaUpdateForm(request.POST, request.FILES, instance=villa)

        if form.is_valid():
            form.save()
            return redirect('villa_detail', villa.id)

    form = VillaUpdateForm(instance=villa)
    return render(request, 'villa/villa_update.html', {'form': form})


def villa_delete_view(request, pk):
    villa = Villa.objects.filter(id=pk).first()
    villa.delete()
    return redirect('index')