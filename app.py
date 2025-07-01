from flask import Flask, request, render_template, jsonify
from invoice_extractor import invoice_extractor
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'Uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract_invoice():
    try:
        # Check if a file was uploaded
        if 'invoice_image' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['invoice_image']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Save the uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Initialize extractor and process the invoice
        extractor = invoice_extractor(llm, filepath)
        metadata_df, items_df = extractor.to_dataframe()
        
        # Convert DataFrames to dictionaries
        metadata = metadata_df.to_dict(orient='records')[0]
        items = items_df.to_dict(orient='records')
        
        # Clean up the uploaded file
        os.remove(filepath)
        
        # Return JSON response
        return jsonify({
            'metadata': metadata,
            'items': items
        })
        
    except Exception as e:
        return jsonify({'error': f'Error processing invoice: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(port=5006, debug=True, host='0.0.0.0')