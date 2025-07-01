FROM python:3.12-slim

WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Create templates directory and copy files
RUN mkdir -p templates invoices
COPY templates/index.html templates/
COPY app.py few_shot_examples.py invoice_extractor.py utils.py .env ./
COPY invoices/6.jpg invoices/
# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python3", "app.py"]