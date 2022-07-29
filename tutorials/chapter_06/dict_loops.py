# firstname, lastanme, age, email, fav_cars, fav_movies

user_info=dict(
    first_name="prince",
    last_name="thomas",
    age="20",
    fav_cars=["bmw-x1","audi r8","bently"],
    fav_movies=["jhonny english", "jhon wick", "mechanic"]
)

for key in user_info:
    print(key)

for key in user_info:
    print(user_info[key])

for value in user_info.values():
    print(value)

for key in user_info:
    print(f"{key}: {user_info[key]}")

print(user_info)