from ninja import NinjaAPI
from app_camera.api import router as camera_router, cam

api = NinjaAPI()

api.add_router('/camera/', camera_router)