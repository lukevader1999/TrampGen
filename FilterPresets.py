from SprungFilter import SprungFilter

exclude_codes = {
    "R R - 0 0 a": "Streckung z. Rücken",
    "S S - 0 0 a": "Streckung z. Sitz",
    "R B r 2 0 a": "Muffel z. Bauch",
}
exclude_codes = exclude_codes.keys()
defaultPresetFilter = SprungFilter(max_rotationen=2, max_schrauben=1, filter_json_path="filter.json", exclude_codes=exclude_codes)

normaleSaltosPresetFilter = SprungFilter(max_rotationen=4, max_schrauben=1, exclude_codes=exclude_codes)

exclude_codes = {
    "R R - 0 0 a": "Streckung z. Rücken",
    "S S - 0 0 a": "Streckung z. Sitz"
}

keinFilterPreset = SprungFilter(exclude_codes=exclude_codes)

#Muffelsausen Plicht 1
def filter_function_muffelsausen_1(sprung):
    if sprung.start == "B" or sprung.ende == "B":
        return False
    if sprung.rotationen > 1:
        return False
    max_schrauben = 1
    if sprung.start == "F" and sprung.ende == "F":
        max_schrauben = 2
    if max_schrauben < sprung.schrauben:
        return False
    return True

muffelsausen1PresetFilter = SprungFilter(
    max_rotationen=1, 
    max_schrauben=2, 
    costum_functions=[filter_function_muffelsausen_1])

#Muffelsausen Plicht 2
def filter_function_muffelsausen_2(sprung):
    included_codes = {
        "R F r 3 0 a": "Muffel"
    }
    if sprung.code in included_codes.keys():
        return True
    if sprung.rotationen > 2:
        return False
    max_schrauben = 1
    if sprung.start == "F" or sprung.ende == "F":
        max_schrauben = 2
    if max_schrauben < sprung.schrauben:
        return False
    return True

muffelsausen2PresetFilter = SprungFilter(
    max_rotationen=2, 
    max_schrauben=2, 
    costum_functions=[filter_function_muffelsausen_2])

#Muffelsausen Plicht 3
muffelsausen3PresetFilter = SprungFilter(
    max_rotationen=4, 
    max_schrauben=2)