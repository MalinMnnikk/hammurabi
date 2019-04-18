from akkadian import *


def is_us_or_us_territory(juris):
    return Or(juris == "United States",
              is_us_territory(juris))


# STATES

alabama = "Alabama"
alaska = "Alaska"
arizona = "Arizona"
arkansas = "Arkansas"
california = "California"
colorado = "Colorado"
connecticut = "Connecticut"
delaware = "Delaware"
florida = "Florida"
georgia = "Georgia"
hawaii = "Hawaii"
idaho = "Idaho"
illinois = "Illinois"
indiana = "Indiana"
iowa = "Iowa"
kansas = "Kansas"
kentucky = "Kentucky"
louisiana = "Louisiana"
maine = "Maine"
maryland = "Maryland"
massachusetts = "Massachusetts"
michigan = "Michigan"
minnesota = "Minnesota"
mississippi = "Mississippi"
missouri = "Missouri"
montana = "Montana"
nebraska = "Nebraska"
nevada = "Nevada"
new_hampshire = "New Hampshire"
new_jersey = "New Jersey"
new_mexico = "New Mexico"
new_york = "New York"
north_carolina = "North Carolina"
north_dakota = "North Dakota"
ohio = "Ohio"
oklahoma = "Oklahoma"
oregon = "Oregon"
pennsylvania = "Pennsylvania"
rhode_island = "Rhode Island"
south_carolina = "South Carolina"
south_dakota = "South Dakota"
tennessee = "Tennessee"
texas = "Texas"
utah = "Utah"
vermont = "Vermont"
virginia = "Virginia"
washington = "Washington"
west_virginia = "West Virginia"
wisconsin = "Wisconsin"
wyoming = "Wyoming"


list_of_states = [alabama, alaska, arizona, arkansas, california, colorado, connecticut, delaware, florida, georgia,
                  hawaii, idaho, illinois, indiana, iowa, kansas, kentucky, louisiana, maine, maryland, massachusetts,
                  michigan, minnesota, mississippi, missouri, montana, nebraska, nevada, new_hampshire, new_jersey,
                  new_mexico, new_york, north_carolina, north_dakota, ohio, oklahoma, oregon, pennsylvania,
                  rhode_island, south_carolina, south_dakota, tennessee, texas, utah, vermont, virginia, washington,
                  west_virginia, wisconsin, wyoming]


# U.S. TERRITORIES


american_samoa = "American Samoa"
guam = "Guam"
n_mariana_islands = "Northern Mariana Islands"
puerto_rico = "Puerto Rico"
us_virgin_islands = "U.S. Virgin Islands"


list_of_territories = [american_samoa, guam, n_mariana_islands, puerto_rico, us_virgin_islands]


def is_us_territory(juris):
    return Or(juris == american_samoa,
              juris == guam,
              juris == n_mariana_islands,
              juris == puerto_rico,
              juris == us_virgin_islands)
