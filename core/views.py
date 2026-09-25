from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, render

from .models import Comunicado


class IntranetLoginView(LoginView):
    template_name = 'core/login.html'


@login_required
def home(request):
    comunicados = Comunicado.objects.select_related('autor')
    contexto = {'comunicados': comunicados}
    return render(request, 'core/home.html', contexto)


@login_required
def comunicado_detalle(request, pk):
    comunicado = get_object_or_404(Comunicado, pk=pk)
    return render(request, 'core/comunicado_detalle.html', {'comunicado': comunicado})
