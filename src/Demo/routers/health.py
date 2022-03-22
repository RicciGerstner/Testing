from fastapi import APIRouter

router = APIRouter()
prefix = ""
path = "/"
tag = {
    "name": "General",
    "description": "General endpoints for service monitoring ✅",
}


@router.get(path, summary="Health check", tags=["General"])
async def root():
    """
    Check if the service is running.
    """
    return {"message": "Service is up and running"}
