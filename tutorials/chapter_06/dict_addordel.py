user_info=dict(
    first_name="prince",
    last_name="thomas",
    age="20",
    fav_cars=["bmw-x1","audi r8","bently"],
    fav_movies=["jhonny english", "jhon wick", "mechanic"]
)

# Add Stuff
user_info["fav_bikes"] = ["ktm", "duke", "hardly davidson", "royal enfield"]
user_info["is_married"] = False

print(user_info)

# Delete Stuff
user_info.popitem() # deletes the last key value pair
user_info.pop("fav_cars") # delets the specified key value pair

print(user_info)