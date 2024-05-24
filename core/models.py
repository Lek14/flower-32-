from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Float, ForeignKey, Integer


from .config import Base


class Flowers(Base):
    __tablename__ = 'flowers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    type: Mapped[str]
    country: Mapped[str] = mapped_column(String(100))
    blooming_season: Mapped[str] = mapped_column(String(50))
    variant: Mapped[str] = mapped_column(String(100))
    price: Mapped[float]
    suppliers: Mapped[list['Suppliers']] = relationship(
        back_populates="flowers",
        secondary="flower_supplier_association",
    )


class FlowerSupplierAssosiation(Base):
    __tablename__ = "flower_supplier_association"

    id: Mapped[str] = mapped_column(Integer, primary_key=True)
    supplier_id: Mapped[int] = mapped_column(ForeignKey("suppliers.id"))
    flower_id: Mapped[int] = mapped_column(ForeignKey("flowers.id"))


class VenderSupllaerAssosion(Base):
    __tablename__ = "vender_supplaer_assosiation"

    id: Mapped[str] = mapped_column(Integer, primary_key=True)
    supplier_id: Mapped[int] = mapped_column(ForeignKey("suppliers.id"))
    vendor_id: Mapped[int] = mapped_column(ForeignKey("vendors.id"))


class Suppliers(Base):
    __tablename__ = 'suppliers'

    id: Mapped[str] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    type_of_farm: Mapped[str] = mapped_column(String(100))
    address: Mapped[str] = mapped_column(String(200))
    flowers: Mapped[list['Flowers']] = relationship(
        back_populates="suppliers",
        secondary="flower_supplier_association",
    )

class Vendors(Base):
    __tablename__ = 'vendors'

    id: Mapped[str] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    address: Mapped[str] = mapped_column(String(200))