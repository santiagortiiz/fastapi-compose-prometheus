"""This is the PWS application initializer."""

from fastapi import FastAPI
from .routers import users, items, hello

app = FastAPI(openapi_url="/api/users-svc/v1/openapi.json")


items_router = items.router

users_router = users.router
users_router.include_router(items_router)

app.include_router(users_router)
app.include_router(hello.router)
