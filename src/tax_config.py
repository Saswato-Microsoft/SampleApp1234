"""Tax configuration provider for the billing system."""

# Tax rates by region (loaded from external config/database)
TAX_RATES = {
    "US-CA": "9.5",
    "US-NY": "8.875",
    "US-TX": "6.25",
    "EU-DE": "19.0",
    "EU-FR": "20.0",
    "IN": "18.0",
}


def get_tax_rate(region):
    """Retrieve the tax rate for a given region.
    
    Bug: Returns the tax rate as a string instead of float.
    The values in TAX_RATES are strings (simulating raw config/DB read)
    and this function does not convert them before returning.
    
    Fix: Return float(TAX_RATES.get(region, "0")) instead of raw string.
    """
    return TAX_RATES.get(region, "0")
