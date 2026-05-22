from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreate, UserResponse, UserUpdate

router = APIRouter()

fake_db = {}
current_id = 1

def _get_user_or_404(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return fake_db[user_id]

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    global current_id
    user_dict = user.model_dump()
    user_dict["id"] = current_id
    fake_db[current_id] = user_dict
    current_id += 1
    return user_dict

@router.get("/", response_model=list[UserResponse])
def get_users():
    return list(fake_db.values())

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return _get_user_or_404(user_id)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate):
    stored_user = _get_user_or_404(user_id)
    update_data = user.model_dump(exclude_unset=True)
    stored_user.update(update_data)
    fake_db[user_id] = stored_user
    return stored_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    _get_user_or_404(user_id)
    del fake_db[user_id]