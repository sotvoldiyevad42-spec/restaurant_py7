from pydantic import BaseModel 
from typing import List
from decimal import Decimal



class CategoryBase(BaseModel):
    name:str


class CategoryCreate(CategoryBase):
    id:int 
   

class MenuItemBase( BaseModel):
    name :str
    price:Decimal
    description:str
    category_id:int


class MenuItemCreate(MenuItemBase):
    pass


class MenuItem(MenuItemBase):
    id:int 

    
    
    
class OrderItemBase(BaseModel):
    menu_item_id=int

    
    
class OrderItemCreate(OrderItemBase):
    pass     
    
class OrderItem(OrderItemBase):
    id:int
    total:Decimal



class OrderBase(BaseModel):
    address:str
    phone_number:str
    status:str="pending"
    
class OrderCreate(OrderBase):
    items:List[OrderItemCreate]


class Order(OrderBase):
