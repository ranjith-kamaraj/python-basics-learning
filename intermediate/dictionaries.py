#Dictionaries
customer = {
    "name": "John Doe",
    "age": 30,
    "email": "john@gmail.com"
}

print(customer["name"])  # Accessing value by key
print(customer.get("age"))  # Accessing value using get method

# Adding a new key-value pair
customer["phone"] = "123-456-7890"
print(customer) 

# Updating an existing key-value pair
customer["email"] = "john.doe@gmail.com"
print(customer)   

# Removing a key-value pair
del customer["age"]
print(customer)
customer.pop("phone")
print(customer)

# Iterating through keys and values
for key, value in customer.items():
    print(f"{key}: {value}")   

# Nested Dictionaries
orders = {
    "order1": {
        "item": "Laptop",
        "quantity": 1,  
        "price": 1200
    },
}
print(orders["order1"]["item"])  # Accessing nested dictionary value 


#Emoji's
emojis = {
    "smile": "😊",
    "heart": "❤️",
    "thumbs_up": "👍"
}
print(emojis["smile"])  # Accessing emoji by key
#ctrl + cmd + space -> in mac

                  


               


                