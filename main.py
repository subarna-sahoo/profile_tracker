from fastapi import FastAPI
from views.tracker import router as tracker_router

app = FastAPI()
app.include_router(tracker_router, prefix="/api")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5050, reload=True)
    # uvicorn main:app --reload