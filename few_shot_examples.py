from utils import read_images
from utils import Invoice
from utils import InvoiceItem

examples = [
    {
        "invoice_example": read_images('invoices/6.jpg'),
        "invoice_data": Invoice(
            invoice_number="0000144804",
            date="2023-11-01",
            vendor_name="Sana Distributors",
            vendor_address="5195 Tomken Road, Mississauga ON L4W 1P1",
            customer_name="Daniel Drug Mart",
            customer_address="1394 Upper Gage Ave, Unit 6, Hamilton ON L8W1E7",
            total_amount=379.78, 
            tax_total=43.69,
            items=[
                InvoiceItem(
                    name="DETTOL SOAP FRESH 100G",
                    quantity=12.0,
                    unit_price=0.89,
                    tax_amount=0.0,  
                    total=10.68
                ),
                InvoiceItem(
                    name="DETTOL SOAP INVIGORATE 100G HB-4202F",
                    quantity=12.0,
                    unit_price=0.99,
                    tax_amount=0.0, 
                    total=11.88
                ),
                InvoiceItem(
                    name="DETTOL SOAP ORIGINAL 100G 3PK",
                    quantity=10.0,
                    unit_price=2.07,
                    tax_amount=0.0, 
                    total=20.70
                ),
                InvoiceItem(
                    name="HALLS - MENTHOL PACK OF 21",
                    quantity=1.0,
                    unit_price = 16.59,
                    tax_amount=0.0,  
                    total=16.59),
                InvoiceItem(
                    name="HALLS ORANGE FLAVORED CANDY 20PK",
                    quantity=1.0,
                    unit_price=15.80,
                    tax_amount=0.0,  
                    total=15.80
                ),
                InvoiceItem(
                    name="HALLS - EXTRA STRONG PACK OF 21",
                    quantity=1.0,
                    unit_price = 16.59,
                    tax_amount=0.0,  
                    total=16.59
                ),
                InvoiceItem(
                    name="T-FALL COPPER CERAMIC JUMBO COOKER WITH GLASS LID #C4108264",
                    quantity=2.0,
                    unit_price=29.99,
                    tax_amount=0.0,  
                    total=59.98
                ),
                InvoiceItem(
                    name="T-FAL STAINLESS STEEL NON-STICK FRYING PAN 24CM #H8680454",
                    quantity=4.0,
                    unit_price=12.99,
                    tax_amount=0.0,  
                    total=51.96
                ),
                InvoiceItem(
                    name="GLASS FRUIT BOWL 9.5\"X9.5\"X4\" #JX-CX",
                    quantity=4.0,
                    unit_price=4.99,
                    tax_amount=0.0,  
                    total=19.96
                ),
                InvoiceItem(
                    name="T-FAL INDUCTION PLATINUM NON-STICK FRYPAN 30CM #H1260774",
                    quantity=2.0,
                    unit_price=19.99,
                    tax_amount=0.0,  
                    total=39.98
                ),
                InvoiceItem(
                    name="DELON RUBBING ALCOHOL 70% 450ML HB-16529",
                    quantity=12.0,
                    unit_price=2.25,
                    tax_amount=0.0,  
                    total=27.00
                ),

                InvoiceItem(
                    name="SESAME ORIGINAL KING SIZE BARS 50G 24 PACK",
                    quantity=3.0,
                    unit_price=14.99,
                    tax_amount=0.0,  
                    total=44.97
                ),

            ]
        ).model_dump_json()
    }
]
