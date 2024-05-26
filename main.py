import uvicorn
import streamlit as st
import requests
from core.config import Base, engine, SessionLocal
from core.models import Suppliers, Vendors, VenderSupllaerAssosion, Flowers

from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from api.views import router
from core.config import get_session


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.include_router(router=router)



def create_vendor_supplier(
    session: Session = SessionLocal()
):

    suppliers_data = [
        (1, "first_supplier", "first_farm", "first_street"),
        (2, "second_supplier", "second_farm", "second_street"),
        (3, "third_supplier", "third_farm", "third_street"),
    ]

    vendors_data = [
        (1, "first_vendor", "first_street"),
        (2, "second_vendor", "second_street"),
        (3, "third_vendor", "third_street"),
    ]
    flowers_data = [
        (1, "first_flower", "first_type", "first_country", "first_season", "first_variant", 10),
        (2, "second_flower", "second_type", "second_country", "second_season", "second_variant", 40),
        (3, "third_flower", "third_type", "third_country", "third_season", "third_variant", 50),
        (4, "fourth_flower", "fourth_type", "fourth_country", "fourth_season", "fourth_variant", 100),
        (5, "fiveth_flower", "fiveth_type", "fiveth_country", "first_season", "fiveth_variant", 5)
    ]


    # создание поставщиков
    suppliers = [
        Suppliers(
            id=supplier[0],
            name=supplier[1],
            type_of_farm=supplier[2],
            address=supplier[3],
        )
        for supplier in suppliers_data
    ]

    #  создание продавцов
    vendors = [
        Vendors(
            id=vendor[0],
            name=vendor[1],
            address=vendor[2],
        )
        for vendor in vendors_data
    ]
    flowers = [
        Flowers(
            id=flower[0],
            name=flower[1],
            type=flower[2],
            country=flower[3],
            blooming_season=flower[4],
            variant=flower[5],
            price=flower[6],

        )
        for flower in flowers_data
    ]

    vendor_supplier_data = [
        (1, 1),
        (1, 2),
        (2, 2)
    ]

    #  добавления заказчикам продовцов
    vendor_supplier_data = [
        VenderSupllaerAssosion(
            supplier_id=vendor_supplier[0],
            vendor_id=vendor_supplier[1],
        )
        for vendor_supplier in vendor_supplier_data
    ]

    session.add_all(vendors)
    session.add_all(suppliers)
    session.add_all(vendor_supplier_data)
    session.add_all(flowers)

    session.commit()
    session.close()


@app.on_event("startup")
def create_db_and_data_db():
    Base.metadata.create_all(bind=engine)
    create_vendor_supplier()


@app.on_event("shutdown")
def delete_all_db():
    Base.metadata.drop_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
