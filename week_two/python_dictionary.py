user_info ={"name":"Paul", "age": 25, "fav_color":"blue"}
name = input("Enter your name: ")
age = input("Enter your age: ")
fav_color = input("Enter your favourite color: ")
user_info["name"] = name
user_info["age"] = age
user_info["fav_color"] = fav_color

for key, value in user_info.items():
    print(key, ":", value)
