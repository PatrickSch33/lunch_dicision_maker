import numpy as np
lunch_option = {"vis_a_vis": {"vegetarian": True, "just_on_friday": False, "close_on_monday": False},
                "habibi": {"vegetarian": True, "just_on_friday": False, "close_on_monday": True},
                "vapiano": {"vegetarian": True, "just_on_friday": False, "close_on_monday": False},
                "doener": {"vegetarian": True, "just_on_friday": False, "close_on_monday": False},
                "asian": {"vegetarian": True, "just_on_friday": False, "close_on_monday": False},
                "asian_big": {"vegetarian": True, "just_on_friday": False, "close_on_monday": False},
                "la_lucha": {"vegetarian": True, "just_on_friday": False, "close_on_monday": False},
                "kuhbar": {"vegetarian": True, "just_on_friday": False, "close_on_monday": False},
                "haroun_s": {"vegetarian": True, "just_on_friday": False, "close_on_monday": False},
                "l_osteria": {"vegetarian": True, "just_on_friday": True, "close_on_monday": False},
                "suppkult": {"vegetarian": True, "just_on_friday": False, "close_on_monday": False},
                "chinese_luisenplatz": {"vegetarian": True, "just_on_friday": False, "close_on_monday": False}}

lunch_option_vegetarian = {k: v for k, v in lunch_option.items() if v["vegetarian"]}
lunch_option_not_on_friday = {k: v for k, v in lunch_option.items() if v["just_on_friday"] is False}
lunch_option_open_on_monday = {k: v for k, v in lunch_option.items() if v["close_on_monday"] is False}

print("Random place: " + np.random.choice(list(lunch_option.keys())))
print("Random VEG place: " + np.random.choice(list(lunch_option_vegetarian.keys())))
print("Random place open on Monday: ", np.random.choice(list(lunch_option_open_on_monday.keys())))
