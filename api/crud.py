from __future__ import annotations

from typing import Type

from sqlalchemy import select, desc
from sqlalchemy.orm import Session, selectinload
from fastapi import Path, Depends, Body

from api.shemas import CreateFlower
from core.models import (
    Flowers,
    Suppliers,
    FlowerSupplierAssosiation,
    Vendors,
    VenderSupllaerAssosion,
)
from core.config import get_session
from core.models import Base



def get_supplier_by_name(
    name_supplier: str = Path(),
    session: Session = Depends(get_session),
) -> Suppliers:
    query = session.query(Suppliers).where(Suppliers.name == name_supplier)
    return query.first()


def get_flower_by_name(
    flower_name: str = Body(),
    session: Session = Depends(get_session),
) -> Flowers:
    query = session.query(Flowers.id).where(Flowers.name == flower_name)
    return query.all()


def create_flower(
    supplier: Suppliers,
    flower_in: CreateFlower,
    session: Session,
) -> Flowers:
    flower = Flowers(
        **flower_in.model_dump()
    )
    session.add(flower)
    session.commit()

    flower_supplier_association = FlowerSupplierAssosiation(
        supplier_id=supplier.id,
        flower_id=flower.id,
    )
    session.add(flower_supplier_association)
    session.commit()

    return flower

def delete_flower(
    flower: Flowers,
    session: Session,
    supplier: Suppliers,
) -> None:
    deletion_flower_query = (
        select(FlowerSupplierAssosiation)
        .where(
            FlowerSupplierAssosiation.supplier_id == supplier.id
            and FlowerSupplierAssosiation.id  == flower.id
        )
    )

    deletion_flower = session.execute(deletion_flower_query).scalar()
    session.delete(deletion_flower)
    session.commit()

def get_all_item_db(
    item: Type[Base],
    session: Session,
) -> Type[Base] | None:
    return session.query(item).all()


def get_all_flower_for_supplier(
    session: Session,
):

    stmt = (
        select(Suppliers)
        .options(
            selectinload(
                Suppliers.flowers
            )
        )
    )
    return session.execute(stmt).scalars().all()


def get_seasonal_flowers(
    seasonal: str,
    session: Session,
):
    return session.query(Flowers).where(Flowers.blooming_season == seasonal).all()


def get_seasonal_country(
    country: str,
    session: Session,
):
    return session.query(Flowers).where(Flowers.country == country).all()


def get_vendor_by_sort(
        sort: bool,
        variant: str,
        session: Session,
):
    stmt = (
        select(Vendors)
        .join(
            VenderSupllaerAssosion,
            VenderSupllaerAssosion.vendor_id == Vendors.id
        )
        .join(
            Suppliers,
            Suppliers.id == VenderSupllaerAssosion.supplier_id,
        )
        .join(
            FlowerSupplierAssosiation,
            FlowerSupplierAssosiation.id == Suppliers.id
        )
        .join(
            Flowers,
            FlowerSupplierAssosiation.flower_id == Flowers.id
        )
    )

    if variant:
        stmt = stmt.where(Flowers.variant == variant)

    if sort:
        stmt = stmt.order_by(
            desc(Flowers.price)
        )

    return session.execute(stmt).scalars().all()


def get_matching_suppliers(session: Session, vendor_id: int):
    # Find all suppliers for the given vendor
    supplier_ids = session.query(VenderSupllaerAssosion.supplier_id).filter(
        VenderSupllaerAssosion.vendor_id == vendor_id).all()
    supplier_ids = [supplier_id[0] for supplier_id in supplier_ids]  # Extract the supplier IDs from the tuples

    # Find all vendors that share the same suppliers
    shared_suppliers = session.query(Suppliers).join(VenderSupllaerAssosion).filter(
        VenderSupllaerAssosion.supplier_id.in_(supplier_ids)).all()

    return shared_suppliers
