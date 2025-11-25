from fastapi import APIRouter, HTTPException
from app.db.supabase_client import supabase
from app.schemas.cargos_schemas import Cargo, CargoCreate
from app.utils.responses import success_response, error_response

router = APIRouter(prefix="/cargos", tags=["Cargos"])

# Obtener todos los cargos 
@router.get("/", response_model=list[Cargo])
def listar_cargos():
    resultado = supabase.table("cargos").select("*").execute()
    return resultado.data

#Obtener pago por ID
@router.get("/{id}", response_model=list[Cargo])
def obtener_cargo(id: int):
    resultado = supabase.table("cargos").select("*").eq("id", id).execute()
    if resultado.data:
        return resultado.data
    raise HTTPException(status_code=404, detail=error_response("Error: Cargo no encontrado"))

#Crear un nuevo Cargo 
@router.post("/", response_model=Cargo)
def crear_pago(cargo: CargoCreate):
    reservacion = supabase.table("reservaciones").select("*").eq("id", cargo.reservation_id).execute().data
    if not reservacion:
        raise HTTPException(status_code=404, detail=error_response("Error: Reservación no encontrada"))
    data = {
        "reservation_id": cargo.reservation_id,
        "description": cargo.description,
        "amount": cargo.amount
    }
    resultado = supabase.table("cargos").insert(data).execute()
    return resultado.data[0]

#Actualizar un Cargo por ID
@router.put("/{id}", response_model=list[Cargo])
def actualizar_cargo(id: int, cargo: CargoCreate):
    resultado = supabase.table("cargos").select("*").eq("id", id).execute()
    if not resultado.data:
        raise HTTPException(status_code=404, detail=error_response("Error: Cargo no encontrado"))
    data = {
        "reservation_id": cargo.reservation_id,
        "description": cargo.description,
        "amount": cargo.amount
    }
    actualizado = supabase.table("cargos").update(data).eq("id", id).execute()
    return actualizado.data[0]

#Eliminar un Cargo por ID
@router.delete("/{id}")
def eliminar_cargo(id: int):
    resulltado = supabase.table("cargos").select("*").eq("id", id).execute()
    if not resulltado.data:
        raise HTTPException(status_code=404, detail=error_response("Error: Cargo no encontrado"))
    data = supabase.table("cargos").delete().eq("id", id).execute().data
    return success_response(data)
