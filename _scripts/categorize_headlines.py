import regions


def categorize_headline_region(headline: str) -> str:
    # Define a dictionary where the keys are regions, and the values are lists of countries/regions associated with that region.
    regions = {
        "International": ["world", "global", "international"],
        "China": regions.CHINA_REGIONS,
        "South Asia": regions.SOUTH_ASIA_REGIONS,
        "Southeast Asia": regions.SOUTHEAST_ASIA_REGIONS,
        "East Asia": regions.EAST_ASIA_REGIONS,
        "Central Asia": regions.CENTRAL_ASIA_REGIONS,
        "West Asia (Middle East)": regions.WEST_ASIA_REGIONS,
        "Russia": regions.RUSSIA_REGIONS,
        "Europe": regions.EUROPE_REGIONS,
        "Africa": regions.AFRICA_REGIONS,
        "North America": regions.NORTH_AMERICA_REGIONS,
        "Latin America and The Caribbean": regions.LATIN_AMERICA_AND_CARIBEAN_REGIONS,
        "Oceania": regions.LATIN_AMERICA_AND_CARIBEAN_REGIONS,
        "Miscellaneous": [],
    }
    # Convert the headline to lowercase for case-insensitive matching
    headline_lower = headline.lower()
    # Loop through each region and its associated keywords
    for region, keywords in regions.items():
        for keyword in keywords:
            if keyword in headline_lower:
                return region
    # If no match is found, return 'Miscellaneous'
    return "Miscellaneous"
