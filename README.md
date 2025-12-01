**Proyecto**
- **Nombre**: Sistema de Gestión de Hotel (backend)
- **Descripción**: API REST construida con FastAPI para gestionar cuartos, huéspedes, reservaciones, pagos y autenticación, usando Supabase como backend de datos.

**Tecnologías**
- **Python**: Aplicación escrita en Python (FastAPI).
- **Framework web**: `fastapi`.
- **Servidor de desarrollo**: `uvicorn`.
- **Base de datos / BaaS**: `supabase` (cliente en `app/db/supabase_client.py`).
- **Autenticación y seguridad**: librerías en `app/core/security.py` y `app/api/auth_api.py`.

**Requisitos**
- Instalar dependencias:

```powershell
& ".venv\Scripts\Activate.ps1" 
python -m venv .venv
pip install -r requirements.txt
```

- Archivo `requirements.txt` incluye:
- `fastapi`, `uvicorn`, `supabase`, `python-dotenv`, `email-validator`, `python-jose`.

**Variables de entorno**
- Crea un archivo `.env` en la raíz con al menos las siguientes variables (los nombres pueden variar según `app/core/config.py`):
- `SUPABASE_URL` — URL del proyecto Supabase.
- `SUPABASE_KEY` — API key de Supabase.
- `SECRET_KEY` — clave secreta para firmas/JWT.
- `ALGORITHM`, `ACCESS_TOKEN_EXPIRE_MINUTES` — configuración de JWT (si aplica).

**Estructura del proyecto**
- **`app/main.py`**: Punto de entrada de la aplicación FastAPI.
- **`app/api/`**: Rutas / endpoints de la API:
	- `auth_api.py` — Autenticación y gestión de tokens.
	- `cargos_api.py` — Endpoints relacionados con cargos (roles o cargos administrativos).
	- `cuartos_api.py` — Endpoints para manejar cuartos (habitaciones).
	- `huespedes_api.py` — Endpoints para huéspedes.
	- `pagos_api.py` — Endpoints para pagos.
	- `reservaciones_api.py` — Endpoints para reservaciones.
- **`app/core/`**:
	- `config.py` — Configuración y carga de variables de entorno.
	- `security.py` — Funciones relacionadas con seguridad (hash, JWT, etc.).
- **`app/crud/`**: Lógica CRUD sobre la fuente de datos (Supabase):
	- `crud_cuartos.py`, `crud_huespedes.py`, `crud_reservaciones.py`.
- **`app/db/`**:
	- `supabase_client.py` — Cliente para conectar y realizar queries contra Supabase.
- **`app/schemas/`**: Pydantic models / schemas para validación de requests/responses:
	- `cargos_schemas.py`, `cuartos_schemas.py`, `huespedes_schemas.py`, `login_schemas.py`, `pagos_schemas.py`, `reservaciones_schemas.py`.
- **`app/services/`**:
	- `reservaciones_services.py` — Lógica de negocio relacionada con reservaciones.
- **`app/utils/`**:
	- `responses.py` — Formateo de respuestas y utilidades.

**Cómo ejecutar (desarrollo)**

1. Crear y activar un entorno virtual:

```powershell
python -m venv .venv
& ".venv\Scripts\Activate.ps1"
```

2. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

3. Exportar las variables de entorno (o crear `.env`) y ejecutar la app con Uvicorn:

```powershell
# Desde la raíz del proyecto
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

4. Abrir la documentación interactiva de la API en: `http://127.0.0.1:8000/docs`

**Rutas principales (archivo -> propósito)**
- `app/api/auth_api.py` — login, refresh tokens, endpoints seguros.
- `app/api/cuartos_api.py` — CRUD y listados de cuartos.
- `app/api/huespedes_api.py` — creación/actualización/consulta de huéspedes.
- `app/api/reservaciones_api.py` — reservar, cancelar, listar reservaciones.
- `app/api/pagos_api.py` — endpoints de pago y comprobantes.
- `app/api/cargos_api.py` — manejo de roles/cargos si aplica.

**Notas de desarrollo**
- La lógica de persistencia está centralizada en `app/crud/*` y usa `app/db/supabase_client.py` para acceder a Supabase.
- Los modelos de entrada/salida están en `app/schemas/` para una validación estricta con Pydantic.
- Para añadir un endpoint nuevo: crear schema en `app/schemas/`, lógica en `app/crud/` o `app/services/`, y ruta en `app/api/`.


**Contacto / Soporte**
- Si necesitas ayuda con la configuración de Supabase o variables, revisa `app/core/config.py` y `app/db/supabase_client.py`.
---