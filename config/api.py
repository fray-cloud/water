from ninja import NinjaAPI
from app_camera.api import router as camera_router
from app_color.api import router as color_router
from app_line.api import router as line_router
from app_text.api import router as text_router
from app_event.api.api import router as event_router

api = NinjaAPI()

api.add_router('/camera/', camera_router)
api.add_router('/color/', color_router)
api.add_router('/line/', line_router)
api.add_router('/text/', text_router)
api.add_router('/event/', event_router)