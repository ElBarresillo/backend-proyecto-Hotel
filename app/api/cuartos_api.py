from fastapi import APIRouter, HTTPException
import app.crud.crud_cuartos as crud
from app.schemas.cuartos_schemas import Cuarto
from app.utils.responses import success_response, error_response

router = APIRouter(prefix="/cuartos", tags=["Cuartos"])

#Obtener todos los cuartos
@router.get("/", summary="Lista Todas las Habitaciones", 
            description="Obtiene la lista Completa de las Habitaciones",
            response_description="Lista de habitaciones.")
def listar_cuartos():
    data = crud.obtenerTodosCuartos()
    return success_response(data)

#Obtener un cuarto
@router.get("/{id}",
            summary="Obtener habitaciones por ID",
            description="Obtiene la informacion de una habitacion especifica por su ID",
            response_description="Datos de la habitacion solicitada.",
            responses={404: {"description": "Habitacion no encontrada"}})
def obtener_cuarto(id: int):
    data = crud.obtenerCuartoId(id)
    return success_response(data)

#Crea un cuarto
@router.post("/", summary="Crea un Cuarto", 
             description="Se Registra una Habitacion en Supabase",
             responses={
                 200: {"description": "Habitacion Creada Correctamente carnal"},
                 400: {"description": "Numero de Habitacion Duplicado/Invalido"}
             })
def crear_cuarto(cuarto: Cuarto):
    if crud.obtenerCuartoNumero(cuarto.number):
        raise HTTPException(status_code=400, detail=error_response("El número de habitación ya existe, ni le muevas"))
    
    data = crud.crearCuarto(cuarto)
    return success_response(data)

#Actualiza un cuarto existente
@router.put("/{id}",
            summary="Actualizar habitacion",
            description="Actualiza la informacion de una habitacion existente por si ID",
            response_description="Habitacion actualizada correctamente.",
            responses={404: {"description": "Habitacion no encontrada"}})
def actualizar_cuarto(id: int, cuarto: Cuarto):
    if not crud.obtenerCuartoId(id): 
        raise HTTPException(status_code=404, detail=error_response("Habitación no encontrada o no Existe"))
    data = crud.updateCuarto(id, cuarto)
    return success_response(data)

#Elimina un cuarto
@router.delete("/{id}",
               summary="Eliminar habitacion",
               description="Elimina una habitacion especifica por su ID.",
               response_description="Habitacion eliminada correctamente.")
def eliminar_cuarto(id: int):
    data = crud.deleteCuarto(id)
    return success_response(data)

# Cambiar estado de la habitacion
@router.put("/{id}/estado", 
            summary="Cambiar estado de la habitación",
            description="Cambia el estado de una habitacion (Disponible, Ocupado, Mantenimiento).",
            response_description="Estado de la habitacion actualizado correctamente.",
            responses={
                400:{"description": "Estado invalido"},
                404: {"description": "Habitacion no encontrada"}
            })
def cambiar_estado_habitacion(id: int, estado: str):
    estados_permitidos = ["Disponible", "Ocupado", "Mantenimiento"]
    if estado not in estados_permitidos:
        raise HTTPException(status_code=400, detail=error_response("Estado inválido"))
    habitacion = crud.obtenerCuartoId(id)
    if not habitacion:
        raise HTTPException(status_code=404, detail=error_response("Habitación no encontrada"))

    data = crud.updateCuartoEstado(id, estado)
    return success_response(data)
