from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

import uvicorn

import asyncio

# importing dataset
from microservices.components.sample_data import product_data




app = FastAPI()

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
        
        
if __name__ == "__main__":
    # Run the FastAPI app
    uvicorn.run(app, host="0.0.0.0", port=1000)   

