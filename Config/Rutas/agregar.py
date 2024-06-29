from fastapi import APIRouter
from Config.Funciones.datos_json import load_data
from Config.Funciones.guardar_json import save_data
from Config.Modelo.pyda import RoleData

router = APIRouter()


@router.post("/api/reaction-roles/")
def update_roles(role_data: RoleData):
    data = load_data()

    
    if "reacion" not in data:
        data["reacion"] = []

    
    new_role = role_data.dict()
    data["reacion"].append(new_role)

    save_data(data)
    return {"message": "Role updated successfully"}