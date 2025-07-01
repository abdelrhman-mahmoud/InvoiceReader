from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import FewShotChatMessagePromptTemplate
from few_shot_examples import examples
from utils import Invoice
import pandas as pd
from utils import read_images
load_dotenv()


class invoice_extractor:
    def __init__(self, llm, image_path):
        self.llm = llm
        self.image_path = image_path
        self.parser = PydanticOutputParser(pydantic_object=Invoice)
        self.few_shot_prompt = ChatPromptTemplate.from_messages([
            {
                'role': 'user',
                'content': [
                    {
                        "type": "image",
                        "source_type": "base64",
                        "data": "{invoice_example}",
                        "mime_type": "image/jpeg",
                    }
                ]
            },
            ('assistant', "{invoice_data}")
        ])

        self.fewshot = FewShotChatMessagePromptTemplate(
            example_prompt=self.few_shot_prompt,
            examples=examples,  # Assumed to be defined elsewhere
        )
        self.history = ChatPromptTemplate.from_messages(
            [
                ('system', '''
                Extract data from this invoice
                follow this output schema {output_schema}
                '''),
                {
                    'role': 'user',
                    'content': [
                        {
                            "type": "image",
                            "source_type": "base64",
                            "data": "{image_data}",
                            "mime_type": "image/jpeg",
                        }
                    ]
                }
            ]
        ).partial(output_schema=self.parser.get_format_instructions())
    
    def extract(self):
        pipeline = self.history | self.llm | self.parser
        output = pipeline.invoke(
            {
                "image_data": read_images(self.image_path), 
            }
        )
        return output
    
    def to_dataframe(self):
        invoice = self.extract()
        
        metadata = {
            'invoice_number': invoice.invoice_number,
            'date': invoice.date,
            'vendor_name': invoice.vendor_name,
            'vendor_address': invoice.vendor_address,
            'customer_name': invoice.customer_name,
            'customer_address': invoice.customer_address,
            'total_amount': invoice.total_amount,
            'tax_total': invoice.tax_total
        }
        metadata_df = pd.DataFrame([metadata])
        
        items_data = [
            {
                'item_name': item.name,
                'quantity': item.quantity,
                'unit_price': item.unit_price,
                'tax_amount': item.tax_amount,
                'total': item.total
            }
            for item in invoice.items
        ]
        items_df = pd.DataFrame(items_data)
        
        return metadata_df, items_df    
    


if __name__ == '__main__':
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0
    )
    image_path = 'invoices/1.jpg'

    extractor = invoice_extractor(llm, image_path)
    metadata_df, items_df = extractor.to_dataframe()
    
    print("Invoice Metadata:")
    print(metadata_df)
    print("\nInvoice Items:")
    print(items_df)