from fastapi import APIRouter, Depends
from app.models.domain import User
from app.api.deps import get_current_user

router = APIRouter()

@router.get("/me")
async def get_my_profile(current_user: User = Depends(get_current_user)):
    return {
        "username": current_user.username,
        "email": current_user.email,
        "status": "Active"
    }

@router.get("/inventory")
async def get_user_inventory(current_user: User = Depends(get_current_user)):
    return {
        "owner": current_user.username,
        "items": ["health_potion", "rusty_sword", "iron_shield"]
    }