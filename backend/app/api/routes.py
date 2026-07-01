from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Welcome to DJOS"}


@router.get("/health")
def health():
    return {"status": "ok", "service": "DJOS API", "version": "0.1.0"}
