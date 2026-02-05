from fastapi import FastAPI
import uvicorn
from routes import route 
import json
from connection import get_db



app = FastAPI()


app.include_router(route)

@app.get("/")
def health():
    return {"status": "I'm alive!!"}

@app.on_event("startup")
def load_data():
    db = get_db()
    collection = db.employees
    file_path = './data/employee_data_advanced.json'
    with open(file_path) as file:
        file_data = json.load(file)
    ins_result = collection.insert_many(file_data)
    print(f"Data inserted to MongoDB. Documents inserted: {len(ins_result.inserted_ids)}")


# if __name__ == "__main__":
#     uvicorn.run("main:app",host="localhost",port=8080,reload=True)