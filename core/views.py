from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, render

from .models import Comunicado, EnlaceSitio, ImagenGaleria


class IntranetLoginView(LoginView):
    template_name = 'core/login.html'


@login_required
def home(request):
    noticias = Comunicado.objects.exclude(
        categoria=Comunicado.Categoria.PARA_TI
    ).select_related('autor')

    contexto = {
        'destacado': noticias.first(),
        'noticias': noticias[1:6],
        'para_ti': Comunicado.objects.filter(
            categoria=Comunicado.Categoria.PARA_TI
        ).first(),
        'enlaces': EnlaceSitio.objects.filter(activo=True),
        'imagenes': ImagenGaleria.objects.all()[:4],
        'sitio_externo_nombre': settings.SITIO_EXTERNO_NOMBRE,
        'sitio_externo_url': settings.SITIO_EXTERNO_URL,
    }
    return render(request, 'core/home.html', contexto)


@login_required
def comunicado_detalle(request, pk):
    comunicado = get_object_or_404(Comunicado, pk=pk)
    return render(request, 'core/comunicado_detalle.html', {'comunicado': comunicado})
