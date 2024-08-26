from fastapi import FastAPI
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
async def root():
  logger.info("Request received - This is a log message from service 1")
  return {"message": "Hello from service 1!"}