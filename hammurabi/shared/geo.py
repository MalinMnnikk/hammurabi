from akkadian import *


# A person's country of residence
def country_of_residence(p):
    return In("str", "shared.country_of_residence", p, None, "What country does {0} live in?")

# The country an entity is located in
def country_location(e):
    return In("str", "shared.country_location", e, None, "What country is {0} located in?")
