import requests

# GET
response = requests.get("https://dummyjson.com/products/1")
post = response.json()

# POST
new_post = {
    "title": "New Product",
    "price": 99.99,
    "description": "A test product",
    "category": "electronics"
}
response = requests.post("https://dummyjson.com/products/add", json=new_post)

# PUT
updated_post = {
    "title": "Updated Product Name",
    "price": 149.99
}
response = requests.put("https://dummyjson.com/products/1", json=updated_post)

#DELETE
response = requests.delete("https://dummyjson.com/products/1")

