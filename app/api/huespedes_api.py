from fastapi import APIRouter, HTTPException
import app.crud.crud_huespedes as crud
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
    data = crud.obtenerTodosHuespedes()
    return success_response(data)

#Crea un huesped
@router.post("/")
def crear_huesped(huesped: Huesped):
    if crud.obtenerHuespedEmail(huesped.email):
       raise HTTPException(status_code=400, detail=error_response("El email ya está registrado"))
    
    if crud.obtenerHuespedPhone(huesped.phone):
       raise HTTPException(status_code=400, detail=error_response("El Telefono ya está registrado"))
    
    data = crud.crearHuesped(huesped)
    return success_response(data)

#Obtengo un solo huesped por id
@router.get("/{id}")
def obtener_huesped(id: int):
    data = crud.obtenerHuespedId(id)
    return success_response(data)

#Actualiza un huesped por id
@router.put("/{id}")
def actualizar_huesped(id: int, huesped: Huesped):
    if not crud.obtenerHuespedId(id):
        raise HTTPException(status_code=404, detail=error_response("Huésped no encontrado o no Existe"))
    data = crud.updateHuesped(id, huesped)
    return success_response(data)

#Elimina un huesped por id
@router.delete("/{id}")
def eliminar_huesped(id: int):
    data = crud.deleteHuesped(id)
    return success_response(data)
