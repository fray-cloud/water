from ninja import Router
from app_camera.models import CameraSetting
from .util.detect import Line

router = Router()
line = Line()