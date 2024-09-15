import pandas as pd

users_db = pd.DataFrame({
    "username": ["admin", "user"],
    "password": ["8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918",
                 "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"]
})

data = pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["John Doe", "Jane Smith", "Bob Johnson"],
        "email": ["john@example.com", "jane@example.com", "bob@example.com"]
    })

