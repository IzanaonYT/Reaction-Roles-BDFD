from fastapi import APIRouter, HTTPException
from Config.Funciones.datos_json import load_data
from Config.Funciones.guardar_json import save_data
from pydantic import BaseModel
from Config.Modelo.deletepy import RoleData
import json

router = APIRouter()




@router.delete("/api/reaction-roles-delete/{index}/")
def delete_role(index: str):
    data = load_data()
    try:
        data["reacion"].pop(int(index))
        save_data(data)
        return {"message": "Role deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Role not found")

