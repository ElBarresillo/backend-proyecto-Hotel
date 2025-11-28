from fastapi import APIRouter, HTTPException
from app.db.supabase_client import supabase
from app.schemas.cargos_schemas import Cargo, CargoCreate
from app.utils.responses import success_response, error_response

router = APIRouter(prefix="/cargos", tags=["Cargos"])

# Obtener todos los cargos 
@router.get("/", response_model=list[Cargo], summary="Listar cargos",
            description="Obtiene la lista de todos los cargos extra registrados en el sistema.",
            response_description="Lista de cargos extra.")
def listar_cargos():
    resultado = supabase.table("cargos").select("*").execute()
    return resultado.data

#Obtener pago por ID
@router.get("/{id}", response_model=list[Cargo], summary="Obtener cargo por ID",
            description="Obtiene la informacion de un cargo extra especifico por su ID.",
            response_description="Datos del cargo extra solicitado.",
            responses={404: {"description": "Cargo no encontrado"}})
def obtener_cargo(id: int):
    resultado = supabase.table("cargos").select("*").eq("id", id).execute()
    if resultado.data:
        return resultado.data
    raise HTTPException(status_code=404, detail=error_response("Error: Cargo no encontrado"))

#Crear un nuevo Cargo 
@router.post("/", response_model=Cargo,
             summary="Crear cargo extra",
             description="Crea un nuevo cargo extra asociado a una reservacion", 
             response_description="Cargo extra creado exitosamente.",
             responses={404: {"description": "Reservacion no encontrada"}})
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
@router.put("/{id}", response_model=list[Cargo],
            summary="Actualizar cargo extra", 
            description="Actualiza la informacion de un cargo extra existente por su ID",
            response_description="Cargo extra actualizado exitosamente.",
            responses={404: {"description": "Cargo no encontrado"}})
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
@router.delete("/{id}",
               summary="Eliminar cargo extra",
               description="Elimina un cargo especifico por su ID.",
               response_description="Cargo extra eliminado exitosamente.",
               responses={404: {"description": "Cargo no encontrado"}})
def eliminar_cargo(id: int):
    resulltado = supabase.table("cargos").select("*").eq("id", id).execute()
    if not resulltado.data:
        raise HTTPException(status_code=404, detail=error_response("Error: Cargo no encontrado"))
    data = supabase.table("cargos").delete().eq("id", id).execute().data
    return success_response(data)
