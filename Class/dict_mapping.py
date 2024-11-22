dog = "cuddly"

dict_map = {
    "hungry": "Refiling food bowl",
    "thirsty": "Refiling water bowl",
    "playful": "playing thug of war",
    "cuddly": "feeding dog treats",
    "other": "reading news paper"
}

owner = dict_map.get(dog, "Reading newsPaper")

print(owner)