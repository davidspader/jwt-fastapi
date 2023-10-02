from fastapi import FastAPI
from app.routes import user_router, test_router

app = FastAPI()

@app.get('/')
def health_check():
    return "It's working"


app.include_router(user_router)
app.include_router(test_router)