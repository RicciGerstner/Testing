import logging
import time

from fastapi import FastAPI
from starlette.requests import Request

from Demo import __DESCRIPTION__, __TITLE__, __VERSION__
from Demo.routers import health


def create_app():
    app = FastAPI(
        title=f"{__TITLE__}",
        description=__DESCRIPTION__,
        version=__VERSION__,
        openapi_tags=[health.tag],
    )
    app.include_router(health.router, prefix=health.prefix)

    request_middleware = app.middleware("http")
    request_middleware(log_requests)

    return app


async def log_requests(request: Request, call_next):
    logging.info(
        f"Request started: Request type = {request.method}, Request path = {request.url.path}"
    )
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time() - start_time
    formatted_end_time = "{0:.2f}".format(end_time)
    logging.info(
        f"Request finished: Status code = {response.status_code}, Duration = {formatted_end_time}s"
    )
    return response
