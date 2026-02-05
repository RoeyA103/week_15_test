from fastapi import FastAPI
import uvicorn
from routes import route 


app = FastAPI()


app.include_router(route)

@app.get("/")
def health():
    return {"status": "I'm alive!!"}


# if __name__ == "__main__":
#     uvicorn.run("main:app",host="localhost",port=8080,reload=True)