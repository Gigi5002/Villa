from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
from .models import Villa
from .filters import VillaFilters
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .form import VillaUpdateForm


def index_view(request):
    """Главная страница с показом активных вилл"""
    try:
        villas = Villa.objects.filter(is_active=True).order_by('-create_date')[:6]
        context = {
            'villas': villas,
            'total_properties': Villa.objects.filter(is_active=True).count(),
        }
        return render(request, 'villa/index.html', context)
    except Exception as e:
        messages.error(request, f"Ошибка загрузки недвижимости: {str(e)}")
        return render(request, 'villa/index.html', {'villas': []})


class VillaListView(ListView):
    """Список всех вилл с фильтрацией и пагинацией"""
    model = Villa
    template_name = 'villa/villa_list.html'
    context_object_name = 'villas'
    paginate_by = 8

    def get_queryset(self):
        """Получаем отфильтрованный queryset"""
        queryset = Villa.objects.filter(is_active=True).order_by('-create_date')
        
        # Применяем фильтры если они есть
        if hasattr(self, 'filterset_class'):
            self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
            queryset = self.filterset.qs
        
        return queryset

    def get_context_data(self, **kwargs):
        """Добавляем дополнительный контекст"""
        context = super().get_context_data(**kwargs)
        
        # Добавляем фильтры в контекст
        if hasattr(self, 'filterset'):
            context['filter'] = self.filterset
        
        # Добавляем общую статистику
        context['total_properties'] = Villa.objects.filter(is_active=True).count()
        context['categories'] = Villa.objects.values_list('category__title', flat=True).distinct()
        
        return context


def villa_detail_view(request, pk):
    """Детальная страница виллы"""
    try:
        villa = get_object_or_404(Villa, id=pk, is_active=True)
        
        # Получаем похожие виллы (по категории и цене)
        similar_villas = Villa.objects.filter(
            is_active=True,
            category=villa.category
        ).exclude(id=pk).order_by('-create_date')[:6]
        
        context = {
            'villa': villa,
            'similar_villas': similar_villas,
        }
        
        return render(request, 'villa/villa_detail.html', context)
        
    except Villa.DoesNotExist:
        messages.error(request, "Недвижимость не найдена или недоступна.")
        return redirect('villa_list')
    except Exception as e:
        messages.error(request, f"Ошибка загрузки недвижимости: {str(e)}")
        return redirect('villa_list')


@login_required
@user_passes_test(lambda u: u.status == 2 or u.is_admin, login_url='/index/')
def villa_update_view(request, pk):
    """Обновление виллы (только для менеджеров и админов)"""
    try:
        villa = get_object_or_404(Villa, id=pk)
        
        if request.method == 'POST':
            form = VillaUpdateForm(request.POST, request.FILES, instance=villa)
            
            if form.is_valid():
                form.save()
                messages.success(request, "Недвижимость успешно обновлена!")
                return redirect('villa_detail', villa.id)
            else:
                messages.error(request, "Пожалуйста, исправьте ошибки ниже.")
        else:
            form = VillaUpdateForm(instance=villa)
        
        context = {
            'form': form,
            'villa': villa,
            'title': 'Редактировать недвижимость'
        }
        
        return render(request, 'villa/villa_update.html', context)
        
    except Villa.DoesNotExist:
        messages.error(request, "Недвижимость не найдена.")
        return redirect('villa_list')
    except Exception as e:
        messages.error(request, f"Ошибка обновления недвижимости: {str(e)}")
        return redirect('villa_list')


@login_required
@user_passes_test(lambda u: u.status == 2 or u.is_admin, login_url='/index/')
def villa_delete_view(request, pk):
    """Удаление виллы (только для менеджеров и админов)"""
    try:
        villa = get_object_or_404(Villa, id=pk)
        
        if request.method == 'POST':
            villa.delete()
            messages.success(request, "Недвижимость успешно удалена!")
            return redirect('villa_list')
        
        # Показываем страницу подтверждения удаления
        context = {
            'villa': villa,
            'title': 'Удалить недвижимость'
        }
        return render(request, 'villa/villa_delete_confirm.html', context)
        
    except Villa.DoesNotExist:
        messages.error(request, "Недвижимость не найдена.")
        return redirect('villa_list')
    except Exception as e:
        messages.error(request, f"Ошибка удаления недвижимости: {str(e)}")
        return redirect('villa_list')
