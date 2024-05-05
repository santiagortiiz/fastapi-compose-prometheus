from fastapi import APIRouter

router = APIRouter(
    prefix="/metrics2",
    tags=["metrics2"],
)


@router.get("/")
def generate_metrics():
    print("Calculate metrics")
    return "Some metrics"
