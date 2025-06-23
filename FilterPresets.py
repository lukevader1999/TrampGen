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