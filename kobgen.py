import random
from mastodon import Mastodon
from api_key import api_access_token

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
    mastodon = Mastodon(
        access_token = api_access_token,
        api_base_url = "https://hellsite.site"
    )
    mastodon.toot("More test posting")

main()
