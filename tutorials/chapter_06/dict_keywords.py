user_info=dict(
    first_name="prince",
    last_name="thomas",
    age="20",
    fav_cars=["bmw-x1","audi r8","bently"],
    fav_movies=["jhonny english", "jhon wick", "mechanic"]
)
if "age" in user_info:
    print("Key Exists")

if "prince" in user_info.values():
    print("Value Exists") 