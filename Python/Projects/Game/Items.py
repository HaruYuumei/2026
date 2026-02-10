
# This is the file with all Items and Informations
#

# Example of item;

# item = {
#     "name" : "name",
#     "description" : "item description",
#     "value" : 0.0,
#     "type" : {"itemType" : "Item type"},
#     "tag" : {"itemTag" : "Item tag"},
#     "size" : 0.0  #meters
# }

# we need a list to hold diferent items?



weapons= [] # everything the player can equip to deal damage and shields
wardrobe = [] # Everything the player can equip on its Body, from clothes to armors


allItems = [weapons,wardrobe]



wood_sword = {
    "name" : "Wooden Sword",
    "description" : "A branch in the shape of a sword",
    "value" : 0.0,
    "type" : {"ItemType": "shortsword"},
    "tag" : {"itemTag" : "Weapons"},
    "size" : 1.0
}

stone_sword = {
    "name" : "Stone Sword",
    "description" : "A handcrafted Stone sword",
    "value" : 1.0,
    "type" : {"ItemType": "shortsword"},
    "tag" : {"itemTag" : "Weapons"},
    "size" : 1.0
}

copper_sword = {
    "name" : "Copper Sword",
    "description" : "A simple copper sword",
    "value" : 3.0,
    "type" : {"ItemType": "shortsword"},
    "tag" : {"itemTag" : "Weapons"},
    "size" : 1.0
}

iron_sword = {
    "name" : "Iron Sword",
    "description" : "A elaborated iron sword",
    "value" : 6.0,
    "type" : {"ItemType": "shortsword"},
    "tag" : {"itemTag" : "Weapons"},
    "size" : 1.0
}

weapons.append(copper_sword)


everything = {
    "Items": {
        
        "Weapons": {
            "iron_sword" : {
                "name" : "Iron Sword",
                "description" : "A elaborated iron sword",
                "value" : 6.0,
                "type" : {"ItemType": "shortsword"},
                "tag" : {"itemTag" : "Weapons"},
                "size" : 1.0
                }
        },
        
        
        "Wardrobe": {
            "name":"itemName"
        }
    }
}

print(everything["Items"]["Weapons"]["iron_sword"])