from aiohttp import web

from app.controllers.healthcheck import healthcheck

ROUTES = [
        web.get('/healthcheck', healthcheck),
        #web.post('/predict', predict),
    ]