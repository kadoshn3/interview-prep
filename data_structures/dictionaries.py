#!/Users/neevekadosh/anaconda3/bin/python3

if __name__=='__main__':
    my_dict = {
        "brand": "Porche",
        "model": "Taycan",
        "year": 2023
        }
    print("Model:", my_dict["model"])
    print("Model:", my_dict.get("model"))
    
    keys = my_dict.keys()
    print("keys:", keys)
    
    values = my_dict.values()
    print("values:", values)
    
    my_dict["color"] = "red"
    print(my_dict)
    my_dict.pop("color")
    print(my_dict)
    
    for key, value in my_dict.items():
        print("items:", key, value)
    for key in my_dict.keys():
        print("keys:", key)
    for value in my_dict.values():
        print("values:", value)
    
    this_dict = my_dict.copy()
    this_dict["model"] = "911"
    
    another_dict = my_dict.copy()
    another_dict["model"] = "cayenne"
    
    cars = {
        "car1" : my_dict,
        "car2" : this_dict,
        "car3" : another_dict
    }
    
    
