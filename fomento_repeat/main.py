from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from . import config
from .resources import lifespan
from .routers import fomento

app = FastAPI(
    title='V2 Fomento',
    debug=config.DEBUG,
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

routers = (fomento.router,)

for router in routers:
    app.include_router(router)
