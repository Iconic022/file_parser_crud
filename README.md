# 📂 File Parser CRUD API  

A FastAPI + Celery + Redis based service for uploading, parsing, and managing text files with CRUD operations.  

---

## 🚀 Setup Instructions  

### 1. Clone the repo  
```bash
git clone https://github.com/Iconic022/file_parser_crud.git
cd file_parser_crud

python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Linux/Mac
source .venv/bin/activate


pip install -r requirements.txt

Start the FastAPI server
uvicorn app.main:app --reload

In a new terminal (with the same venv activated):

celery -A app.tasks.celery worker --loglevel=info

📖 API Documentation

When the server is running, FastAPI automatically generates docs at:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

🛠️ API Endpoints with Sample Requests & Responses
1. Upload File

POST /files
Upload a text file for parsing.

cURL Example

curl -X POST "http://127.0.0.1:8000/files" -F "file=@README.md"


Response

{
  "id": 1,
  "filename": "README.md",
  "status": "uploaded"
}

2. List Files

GET /files

Sample Request

curl -X GET "http://127.0.0.1:8000/files"


Response

[
  {
    "id": 1,
    "filename": "README.md",
    "status": "parsed"
  }
]

3. Get File by ID

GET /files/{file_id}

Sample Request

curl -X GET "http://127.0.0.1:8000/files/1"


Response

{
  "id": 1,
  "filename": "README.md",
  "content": "Hello World! This is a sample file."
}

4. Update File Metadata

PUT /files/{file_id}

Sample Request

curl -X PUT "http://127.0.0.1:8000/files/1" \
  -H "Content-Type: application/json" \
  -d '{"filename": "updated_file.txt"}'


Response

{
  "id": 1,
  "filename": "updated_file.txt",
  "status": "parsed"
}

5. Delete File

DELETE /files/{file_id}

Sample Request

curl -X DELETE "http://127.0.0.1:8000/files/1"


Response

{ "message": "File deleted successfully" }

✅ Notes

Ensure Redis is running before starting Celery.

Uploaded files are stored in the uploads/ folder.

The app is ready for extension (e.g., file type validation, authentication).

Works with both curl and Postman for testing.


---

👉 This file is **ready to drop into your repo as `README.md`**.  

Do you also want me to **add the Postman collection JSON inline inside the README** (so everything is in one file
