from akkadian import *
import hammurabi.shared.dataprivacy as dp
import hammurabi.us.shared.geo as geo


# Video Privacy Protection Act of 1988 (VPPA)
# 18 U.S.C. 2710


# Applicability


# Assuming a broad territorial scope
def vppa_applies(data):
    return And(EffectiveFrom('1988-11-05'),
               Or(geo.is_us_or_us_territory(dp.processor_country(data)),
                  geo.is_us_or_us_territory(dp.controller_country(data)),
                  geo.is_us_or_us_territory(dp.subject_country(data))),
               industry_is("Video rental or distribution"))





# Sec. 2710(b)(1) - Non-disclosure requirement
# violatesVPPAb1 := activitiesAreAny[{"Disclosure", "Publication", "Transfer"}] &&
# contentIsAny[{"Address", "Authenticating information",
# "Customer purchase history", "Date of birth", "Gender", "IP address", "Name",
# "Online identifier", "Telephone number", "Location", "Unique identifier"}] &&
# ! disclosureExceptionAppliesVPPA

# Sec. 2710(b)(2) - Exceptions to non-disclosure requirement
# disclosureExceptionAppliesVPPA :=
# (* (b)(2)(B) *)
# subjectConsent ||
# (* (b)(2)(C), (b)(3) *)
# processingForAny[
# {"Criminal procedure", "Law enforcement", "Public security"}] ||
# (* (b)(2)(D) *)
# contentIsAny[{"Name", "Address"}] &&
# ! contentIs["Customer purchase history"] || processingFor["Marketing"] ||
# (* (b)(2)(F) *)
# processingForAny[
# {"Compliance with legal obligation", "Legal proceeding or claim"}]

# Sec. 2710(e) - Destruction of old records
# riskOfViolatingVPPAsec2710e := activityIs["Storage"]