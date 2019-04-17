from akkadian import *


def is_us_or_us_territory(juris):
    return Or(juris == "United States",
              is_us_territory(juris))


def is_us_territory(juris):
    return Or(juris == "American Samoa",
              juris == "Guam",
              juris == "Northern Mariana Islands",
              juris == "Puerto Rico",
              juris == "U.S. Virgin Islands")
