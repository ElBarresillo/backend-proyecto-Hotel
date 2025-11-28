from fastapi import APIRouter, HTTPException, Depends, Header
from supabase import create_client
from app.core.config import SUPABASE_URL, SUPABASE_KEY
from app.schemas.login_schemas import LoginBase
from app.utils.responses import error_response
from app.core.security import verificar_token

router = APIRouter(prefix="/auth", tags=["Auth"])

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


@router.post ("/login", summary="Iniciar sesion", description="Autentica a un usuario y deveulve tokens de acceso", 
              response_description="Login exitoso", responses={404: {"description": "Credenciales invalidas"}})
def login(data: LoginBase):
    resultado = supabase.auth.sign_in_with_password({
        "email": data.email,
        "password": data.password
    })
    if not resultado.session:
        raise HTTPException(status_code=404, detail=error_response("Error: Credenciales inválidas"))
    return {
        "message": "Login Exitoso",
        "access_token": resultado.session.access_token,
        "refresh_token": resultado.session.refresh_token,
        "user_id": resultado.session.user.id
    }

@router.get("/login", summary="Listar empleados", description="Devuelve la lista de empleados registrados en el sistema.",
            response_description="Lista de empleados")
def listar_empleados():
    resultado = supabase.table("perfiles").select("*").execute() 
    return resultado.data

@router.get("/protected", summary="Ruta protegida", description="Ruta que requiere autenticacion mediante token JWT.",
            response_description="Acceso concedido si el usuario esta autenticado.")
async def protected_route(user=Depends(verificar_token)):
    return {"message": "Acceso concedido", "user": user}

@router.get("/protected-test", summary="Test de header Authorization", description="Ruta de prueba para mostrar el header Authorization recibido",
            response_description="Header Authorization recibido.")
async def test_route(Authorization: str = Header(None)):
    print("HEADER EN RUTA:", Authorization)
    return {"recibido": Authorization}