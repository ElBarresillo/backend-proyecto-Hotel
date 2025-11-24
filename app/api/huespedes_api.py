from fastapi import APIRouter, HTTPException
from app.db.supabase_client import supabase
from app.schemas.huespedes_schemas import Huesped
from app.utils.responses import success_response, error_response

router = APIRouter(prefix="/huespedes", tags=["Huespedes"])

#Obtengo todos los Huespedes
@router.get("/", summary="Registar un Huesped", description="Crea un registro de huesped en supabase",
            responses={
                200: {"description": "Huesped creado Correctamente"},
                400: {"description": "Email Duplicado/Invalido"}
            })
def listar_huespedes():
    data = supabase.table("huespedes").select("*").execute().data
    return success_response(data)
############# Fin de Obtener los huespedes

#Crea un huesped
@router.post("/")
def crear_huesped(huesped: Huesped):
    siExisteEmail = supabase.table("huespedes").select("*").eq("email", huesped.email).execute().data
    if siExisteEmail:
       raise HTTPException(status_code=400, detail=error_response("El email ya está registrado"))
    
    siExisteTelefono = supabase.table("huespedes").select("*").eq("phone", huesped.phone).execute().data
    if siExisteTelefono:
       raise HTTPException(status_code=400, detail=error_response("El Telefono ya está registrado"))
    data = supabase.table("huespedes").insert(huesped.dict()).execute().data
    return success_response(data)
############# Fin de Crear un Huesped

#Obtengo un solo huesped por id
@router.get("/{id}")
def obtener_huesped(id: int):
    data = supabase.table("huespedes").select("*").eq("id", id).execute().data
    return success_response(data)

#Actualiza un huesped por id
@router.put("/{id}")
def actualizar_huesped(id: int, huesped: Huesped):
    siExiste = supabase.table("huespedes").select("*").eq("id", id).execute().data
    if not siExiste:
        raise HTTPException(status_code=404, detail=error_response("Huésped no encontrado o no Existe"))
    data = supabase.table("huespedes").update(huesped.dict()).eq("id", id).execute().data
    return success_response(data)

#Elimina un huesped por id
@router.delete("/{id}")
def eliminar_huesped(id: int):
    data = supabase.table("huespedes").delete().eq("id", id).execute().data
    return success_response(data)
