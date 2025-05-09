import logging, uvicorn, asyncio, os
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from fastapi import FastAPI
from bot import *
from database import *
from controllers import router

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')    
    await Db_Connect()
    asyncio.create_task(bot_run())
    yield
    await Db_Disconnect()
    await bot_stop()

app = FastAPI(lifespan=lifespan, swagger_ui_parameters={"syntaxHighlight": False})
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=int(os.environ['PORT']))