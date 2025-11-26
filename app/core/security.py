from fastapi import status, HTTPException, Header
from app.utils.responses import error_response
from fastapi.security import OAuth2PasswordBearer
from supabase import create_client
from app.core.config import SUPABASE_URL, SUPABASE_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

async def verificar_token(Authorization: str = Header(None)):
    print("Token recibido:", Authorization)  # Línea de depuración  
    if Authorization is None:
        raise HTTPException(
            status_code=404,
            detail=error_response("Error: Token de autorización no proporcionado"),
        )
    try:
        token = Authorization.split(" ")[1]
        user = supabase.auth.get_user(token)
        if user.user is None:
            raise HTTPException(
                status_code=404,
                detail=error_response("Error: Token inválido o expirado"),
            )
        return user.user
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=error_response("Error: Token inválido o expirado"),
        )