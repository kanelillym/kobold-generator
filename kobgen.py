import random

ATTRIBUTES = {
    "color_primary"   : "teal",
    "color_secondary" : "peridot",
    "color_pattern"   : "speckles",
    "eye_color"       : "red",
    "snout_shape"     : "wedge",
    "horns_count"     : 2,
    "horns_type"      : "straight",
    "tail_type"       : "long",
    "tail_action"     : "wag"
    }

def main():
    random.seed()
    print(random.randrange(1,10))

main()
