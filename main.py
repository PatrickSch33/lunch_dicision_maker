import numpy as np
lunch_option = {"soup": {"vegetarian": True, "just_on_friday": False},
                "habibi": {"vegetarian": True, "just_on_friday": False},
                "vapiano": {"vegetarian": True, "just_on_friday": False},
                "doener": {"vegetarian": True, "just_on_friday": False},
                "asian": {"vegetarian": True, "just_on_friday": False},
                "la_lucha": {"vegetarian": True, "just_on_friday": False},
                "kuhbar": {"vegetarian": True, "just_on_friday": False},
                "losteria": {"vegetarian": True, "just_on_friday": True}}

lunch_option_vegetarian = {k: v for k, v in lunch_option.iteritems() if v["vegetarian"]}
lunch_option_not_on_friday = {k: v for k, v in lunch_option.iteritems() if v["just_on_friday"] is False}

random_place = np.random.choice(lunch_option.keys())
print(random_place)


