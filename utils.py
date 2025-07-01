
import base64
from typing import Optional, List

from pydantic import BaseModel, Field


class InvoiceItem(BaseModel):
    name: Optional[str] = Field(description="The name or description of the item or service")
    quantity: Optional[float] = Field(description="The quantity of the item or service")
    unit_price: Optional[float] = Field(description="The price per unit of the item or service" )
    tax_amount: Optional[float] = Field(default=0.0, description="The tax amount applied to this item")
    total: Optional[float] = Field (description="The total cost for this item (quantity * unit_price + tax_amount)")

class Invoice(BaseModel):
    invoice_number: Optional[str] = Field(description="Unique identifier for the invoice",default='')
    date: Optional[str] = Field(description="Date the invoice was issued (e.g., YYYY-MM-DD)", default= '')
    vendor_name: Optional[str] = Field(description="Name of the vendor issuing the invoice", default= '')
    vendor_address: Optional[str] = Field(default="", description="Address of the vendor")
    customer_name: Optional[str] = Field(description="Name of the customer or client",default= '')
    customer_address: Optional[str] = Field(default="", description="Address of the customer")
    total_amount: Optional[float] = Field(default=0.0, description="Total amount for all items including taxes")
    tax_total: Optional[float] = Field(default=0.0, description="Total tax amount for all items")
    items: List[InvoiceItem] = Field(..., description="List of items or services included in the invoice")

def read_images(image_path):
    with open(image_path, "rb")as img:
        return base64.b64encode(img.read()).decode('utf-8')
    