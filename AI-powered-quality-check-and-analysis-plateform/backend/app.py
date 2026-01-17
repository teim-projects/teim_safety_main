from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from routers import auth, ppe, machine, dashboard, notifications, face_routes
from db.database import init_db

app = FastAPI(title="PPE Detection + Auth API", version="1.0")

# Initialize DB
init_db()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files (if used by backend)
app.mount("/static", StaticFiles(directory="static"), name="static")

# ================= ROUTERS =================

# ✅ AUTH (FIXED)
app.include_router(auth.router, prefix="/api", tags=["auth"])

# ✅ PPE MODEL
app.include_router(ppe.router, prefix="/predict", tags=["ppe"])

# ✅ MACHINE MODEL
app.include_router(machine.router, prefix="/predict_machine", tags=["machine"])

# ✅ DASHBOARD + NOTIFICATIONS (they already use /api in frontend)
app.include_router(dashboard.router, prefix="/api")
app.include_router(notifications.router, prefix="/api")

# ✅ FACE ROUTES
app.include_router(face_routes.router, prefix="/face", tags=["face"])

@app.get("/")
def root():
    return {"message": "API running"}
