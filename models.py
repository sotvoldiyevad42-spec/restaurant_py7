from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Boolean, ForeignKey, Numeric

from database import Base

class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    items: Mapped[Menu] = relationship(back_populates="category")    

class Menu(Base):
    __tablename__ = 'menu_items'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    priece: Mapped[float] = mapped_column(Numeric, (10,29))
    description: Mapped[str] = mapped_column(String(200))
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category: Mapped["Category"] = relationship(back_populates="items")    

class Orders(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address: Mapped[str] = mapped_column(String(length=100))
    total: Mapped[float] = mapped_column(Numeric(10,2))
    phone_number: Mapped[str] = mapped_column(20)
    status: Mapped[str] = mapped_column(String(50), default="pending")
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    
    items: Mapped[Order_item] = relationship(back_populates="order")

    
class Order_item(Base):
    __tablename__ = 'order_items'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    quamtity: Mapped[str] = mapped_column(Integer (default=1))
    total: Mapped[float] = mapped_column(Numeric(10,20))
    order: Mapped[int] = mapped_column(ForeignKey('users.id'))
    menu_item: Mapped["Menu"] = relationship()
    menu_item_id: Mapped[int] = mapped_column(ForeignKey('menu_items.id'))
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id'))
    
    order: Mapped["Orders"] = relationship(back_populates="items")
