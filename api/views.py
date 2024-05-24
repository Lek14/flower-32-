from fastapi import APIRouter, status, Depends, HTTPException

from core.config import get_session
from .shemas import CreateFlower, ShowFlower
from sqlalchemy.orm import Session
from . import crud as api_crud

from core.models import Flowers, Suppliers, Vendors

router = APIRouter()

@router.post(
    "/create_flower/{name_supplier}",
    status_code=status.HTTP_201_CREATED,
    response_model=ShowFlower,
)
def create_flower(
    flower_in: CreateFlower,
    session: Session = Depends(get_session),
    supplier: Suppliers | None = Depends(api_crud.get_supplier_by_name),
) -> Flowers:

    if not supplier:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Объект не найден по имени"
        )

    return api_crud.create_flower(
        supplier=supplier,
        flower_in=flower_in,
        session=session,
    )


@router.delete(
    "/delete_flower/{name_supplier}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_flower(
    flower: Flowers = Depends(api_crud.get_flower_by_name),
    session: Session = Depends(get_session),
    supplier: Suppliers | None = Depends(api_crud.get_supplier_by_name),
):
    if not supplier or not flower:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Объект не найден по имени"
        )

    api_crud.delete_flower(
        flower=flower,
        session=session,
        supplier=supplier,
    )

@router.get("/get_all_flowers", status_code=status.HTTP_200_OK)
def get_all_flowers(
    session: Session = Depends(get_session),
):
    return api_crud.get_all_item_db(
        item=Flowers,
        session=session,
    )

@router.get("/get_all_supplier", status_code=status.HTTP_200_OK)
def get_all_supplier(
    session: Session = Depends(get_session),
):
    return api_crud.get_all_item_db(
        item=Suppliers,
        session=session,
    )

@router.get("/get_all_vendors", status_code=status.HTTP_200_OK)
def get_all_vendors(
    session: Session = Depends(get_session),
):
    return api_crud.get_all_item_db(
        item=Vendors,
        session=session,
    )


@router.get("/get_all_flowers_for_suppliers", status_code=status.HTTP_200_OK)
def get_all_flowers_for_suppliers(
    session: Session = Depends(get_session)
):
    return api_crud.get_all_flower_for_supplier(
        session=session,
    )

@router.get("/get_seasonal_flowers/{seasonal}", status_code=status.HTTP_200_OK)
def get_seasonal_flowers(
    seasonal: str,
    session: Session = Depends(get_session)
):
    return api_crud.get_seasonal_flowers(
        seasonal=seasonal,
        session=session,
    )


@router.get("/get_flowers_for_country/{country}")
def get_seasonal_country(
    country: str,
    session: Session = Depends(get_session)
):
    return api_crud.get_seasonal_country(
        country=country,
        session=session,
    )

@router.get("/get_vendors")
def get_vendors(
    sort: bool = False,
    variant: str | None = None,
    session: Session = Depends(get_session)
):
    return api_crud.get_vendors(
        sort=sort,
        variant=variant,
        session=session,
    )
