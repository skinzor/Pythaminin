scientists = [
    {"name": "Ada Lovelace", "field": "Mathematics", "birth": 1815, "nobel": False},
    {"name": "Marie Curie", "field": "Mathematics", "birth": 1882, "nobel": False}
]

print(scientists[0]["name"])
scientists[0]["name"] = "Ada Hatelace"
print(scientists[0]["name"])
