users = [
    {"id": 1, "role": "admin", "name": "Vasiliy"},
    {"id": 2, "role": "manager", "name": "Aleksandr"},
    {"id": 3, "role": "saler", "name": "Arseniy", "degree": [
        {"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"}]},
]

users2 = [
    {"id": 1, "role": "admin", "name": "Vasiliy"},
    {"id": 2, "role": "manager", "name": "Aleksandr"},
    {"id": 3, "role": "saler", "name": "Arseniy"},
]

f_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC",
        "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC",
        "side": "sell", "price": 125, "amount": 2.12},
]
