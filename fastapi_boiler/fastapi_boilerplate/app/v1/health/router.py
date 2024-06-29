from fastapi.routing import APIRouter

router = APIRouter(prefix='/health', tags=['health'])


@router.get("")
def health():
    return {
        "status": "success"
    }
