# from typing import List
# import schemas
# from fastapi import APIRouter, BackgroundTasks, FastAPI
# from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
# from pydantic import BaseModel, EmailStr
# from starlette.responses import JSONResponse


# router = APIRouter(
#     prefix='/email',
#     tags=["email"]
# )

# conf = ConnectionConfig(
#     MAIL_USERNAME = "vocabrise@gmail.com",
#     MAIL_PASSWORD = "srkfoqwzvhpwotvv",
#     MAIL_FROM = "vocabrise@gmail.com",
#     MAIL_PORT = 465,
#     MAIL_SERVER = 'smtp.gmail.com',
#     MAIL_STARTTLS = False,
#     MAIL_SSL_TLS = True,
#     USE_CREDENTIALS = True,
#     VALIDATE_CERTS = True    
#     )

# html = """
#     <p>Thanks for using Fastapi-mail</p>
# """

# @router.post("/email")
# async def simple_send(email: schemas.EmailSchema) -> JSONResponse:
#     message = MessageSchema(
#         subject="Fastapi-Mail module",
#         recipients=email.model_dump().get("email"),
#         body=html,
#         subtype=MessageType.html)
    
#     fm = FastMail(conf)
#     await fm.send_message(message)
#     return JSONResponse(status_code=200, content={"message": "email has been sent"})