import numpy as np
lunch_option = {"soup": {"vegetarian": True},
                "habibi": {"vegetarian": True},
                "vapiano": {"vegetarian": True},
                "doener": {"vegetarian": True},
                "asian": {"vegetarian": True},
                "la_lucha": {"vegetarian": True},
                "kuhbar": {"vegetarian": True}}

lunch_option_vegatarian = {k: v for k, v in lunch_option.iteritems() if v["vegetarian"]}

random_place = np.random.choice(lunch_option.keys())
print(random_place)


