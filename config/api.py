from ninja import NinjaAPI
from app_camera.api import router as camera_router
from app_color.api import router as color_router

api = NinjaAPI()

api.add_router('/camera/', camera_router)
api.add_router('/color/', color_router)