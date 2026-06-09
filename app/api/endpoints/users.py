from fastapi import APIRouter, HTTPException
from app.models.schemas import UserCreate, UserUpdate, UserResponse
from app.db.fake_db import users_db

router = APIRouter()

@router.get("/", response_model=list[UserResponse])
async def get_users():
    return list(users_db.values())

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@router.post("/", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate):
    new_id = len(users_db) + 1
    user_dict = user.model_dump()
    user_dict["id"] = new_id
    users_db[new_id] = user_dict
    return user_dict

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_update: UserUpdate):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    stored_user = users_db[user_id]
    update_data = user_update.model_dump(exclude_unset=True)
    stored_user.update(update_data)
    users_db[user_id] = stored_user
    return stored_user

@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]