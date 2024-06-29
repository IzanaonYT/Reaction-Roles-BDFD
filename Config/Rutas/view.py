from fastapi import APIRouter
from fastapi.responses import Response
import json
from Config.Funciones.datos_json import load_data

router = APIRouter()

@router.get("/api/get-reaction-roles/")
def read_roles():
    data = load_data()
    n = json.dumps(data, indent=4)
    return Response(n, media_type="application/json")
