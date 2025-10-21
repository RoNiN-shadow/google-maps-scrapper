from fastapi import FastAPI
from utils.save_data import save_data
app = FastAPI()


@app.get("/scraper")
async def scraper():
    save_data()
    return ...
