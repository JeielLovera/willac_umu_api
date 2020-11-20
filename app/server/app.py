from fastapi import FastAPI
from server.routes.estudiantes import router as EstudiantesRouter
from server.routes.training import router as TrainingRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="WILLAC UMU REST API")

app.include_router(EstudiantesRouter, tags=["Estudiantes"], prefix="/estudiantes")
app.include_router(TrainingRouter, tags=["Training"], prefix="/training")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Bienvenidos al himalaya!!!"}



