from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

import uvicorn

import asyncio

# Middleware for CORS
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles



# importing dataset
from microservices.components.sample_data import product_data
from helper import get_image_list




app = FastAPI()


# Origin for CORS
origins = [
    "http://localhost:5173",  # Allow requests from your frontend origin
]

# Middleware for CORS
# This allows your frontend to make requests to the FastAPI backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Base model data type for product 
class Product(BaseModel):
    id: int
    qty : int 
    
    name : str
    price : int
    desc: str
    img_url: str
    
    
# Endpoint for GET and POST requests
@app.get("/")
def read_root():
    return {"Ping": "Pong"}

@app.get("/products")
def get_products():
    data = product_data()
    return data

@app.get("/prducts/{product_id}")
def get_productById(product_id: int):
    data = product_data()
    for product in data:
        if product['product_id'] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.get("/images/{image_id}")
def get_imageById(image_id: int):
    image_data = get_image_list("./microservices/components/images")
    for image in image_data:
        if image_id == int(image.split('-')[1].split('.')[0]):
            return FileResponse(f"./microservices/components/images/{image}")
    raise HTTPException(status_code=404, detail="Image not found")
    



    
 




if __name__ == "__main__":
    # Run the FastAPI app
    uvicorn.run(app, host="0.0.0.0", port=8000)   

