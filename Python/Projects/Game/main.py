import Items

player = {
    "name":"name",
    "inventory": []

}

player["inventory"].append(Items.weapons[0])
print(player["inventory"][0]["name"])
