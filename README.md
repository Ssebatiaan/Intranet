# Intranet — base del proyecto (Django)

Proyecto base de intranet construido con Django, listo para levantar en local y
empezar a agregar funcionalidad.

## ¿Qué trae ya funcionando?

- Login / logout de usuarios (`/login/`, `/logout/`)
- Página de inicio protegida (`/`) que lista **comunicados**
- Detalle de cada comunicado (`/comunicados/<id>/`)
- Panel de administración de Django (`/admin/`) para crear comunicados sin
  necesidad de código
- Diseño propio (tipografía Fraunces + Work Sans, paleta personalizada) en
  `static/css/base.css`

## Estructura del proyecto

```
intranet/
├── manage.py
├── requirements.txt
├── config/              # configuración del proyecto (settings, urls raíz)
├── core/                # app principal: modelo Comunicado, vistas, templates
│   ├── models.py        # modelo Comunicado
│   ├── views.py         # login, home, detalle
│   ├── urls.py
│   └── templates/core/
└── static/css/base.css  # estilos globales
```

## Cómo levantarlo

1. Crear y activar un entorno virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # en Windows: venv\Scripts\activate
   ```

2. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Aplicar las migraciones (crea la base de datos SQLite):

   ```bash
   python manage.py migrate
   ```

4. Crear un usuario administrador para poder entrar y usar el panel `/admin/`:

   ```bash
   python manage.py createsuperuser
   ```

5. Levantar el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

6. Abrir <http://127.0.0.1:8000/>, iniciar sesión con el usuario creado, y
   entrar a <http://127.0.0.1:8000/admin/> para crear el primer comunicado.

## Próximos pasos sugeridos

- Nueva app para **documentos** (subir/descargar archivos por área)
- Nueva app para **directorio de empleados**
- Permisos por rol (grupos de Django: RRHH, TI, empleados)
- Pasar de SQLite a PostgreSQL cuando salga de desarrollo
