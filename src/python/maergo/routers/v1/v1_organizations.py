from fastapi import APIRouter, status

router = APIRouter(
  prefix="/organizations",
  tags=["organizations"],
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_organization():
  return "create organization"


@router.get("/organization/{id}")
def read_organization(id: int):
  return f"read organization with id {id}"


@router.put("/todo/{id}")
def update_organization(id: int):
  return f"update organization with id {id}"


@router.delete("/todo/{id}")
def delete_organization(id: int):
  return f"delete organization with id {id}"
