from fastapi import APIRouter, HTTPException
import app.crud.crud_cuartos as crud
from app.schemas.cuartos_schemas import Cuarto
from app.utils.responses import success_response, error_response

router = APIRouter(prefix="/cuartos", tags=["Cuartos"])

#Obtener todos los cuartos
@router.get("/", summary="Lista Todas las Habitaciones", description="Obtiene la lista Completa de las Habitaciones")
def listar_cuartos():
    data = crud.obtenerTodosCuartos()
    return success_response(data)

#Obtener un cuarto
@router.get("/{id}")
def obtener_cuarto(id: int):
    data = crud.obtenerCuartoId(id)
    return success_response(data)
################ Fin de Obtener un Cuarto

#Crea un cuarto
@router.post("/", summary="Crea un Cuarto", description="Se Registra una Habitacion en Supabase",
             responses={
                 200: {"description": "Habitacion Creada Correctamente carnal"},
                 400: {"description": "Numero de Habitacion Duplicado/Invalido"}
             })
def crear_cuarto(cuarto: Cuarto):
    if crud.obtenerCuartoNumero(cuarto.number):
        raise HTTPException(status_code=400, detail=error_response("El número de habitación ya existe, ni le muevas"))
    
    data = crud.crearCuarto(cuarto)
    return success_response(data)
################ Fin de Crear un Cuarto

#Actualiza un cuarto existente
@router.put("/{id}")
def actualizar_cuarto(id: int, cuarto: Cuarto):
    if not crud.obtenerCuartoId(id): #verifico si ya existe una habitacion con ese numero
        raise HTTPException(status_code=404, detail=error_response("Habitación no encontrada o no Existe"))
    data = crud.updateCuarto(id, cuarto)
    return success_response(data)
################ Fin de Actualizar un Cuarto

#Elimina un cuarto
@router.delete("/{id}")
def eliminar_cuarto(id: int):
    data = crud.deleteCuarto(id)
    return success_response(data)
################ Fin de Eliminar un Cuarto

# Estatus para la Habitacion
@router.put("/{id}/estado", summary="Cambiar estado de la habitación")
def cambiar_estado_habitacion(id: int, estado: str):
    # Validar que el estado sea permitido
    estados_permitidos = ["Disponible", "Ocupado", "Mantenimiento"]
    if estado not in estados_permitidos:
        raise HTTPException(status_code=400, detail=error_response("Estado inválido"))

    # Verificar que la habitación existe
    habitacion = crud.obtenerCuartoId(id)
    if not habitacion:
        raise HTTPException(status_code=404, detail=error_response("Habitación no encontrada"))

    data = crud.updateCuartoEstado(id, estado)
    return success_response(data)
