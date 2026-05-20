"""User profile parser that extracts and normalizes user data from raw API responses."""


def parse_user_profile(raw_data):
    """Parse raw API response into a normalized user profile dict.
    
    Bug: When the API returns a user with 'name' field instead of
    'first_name'/'last_name' (e.g., for OAuth/social logins), this
    function still constructs the profile with only 'full_name' key
    but does NOT include 'first_name' and 'last_name' as separate keys.
    """
    profile = {}

    if "first_name" in raw_data and "last_name" in raw_data:
        profile["first_name"] = raw_data["first_name"]
        profile["last_name"] = raw_data["last_name"]
        profile["full_name"] = f"{raw_data['first_name']} {raw_data['last_name']}"
    elif "name" in raw_data:
        # Bug: Only sets 'full_name', does NOT split into first_name/last_name
        profile["full_name"] = raw_data["name"]

    profile["email"] = raw_data.get("email", "")
    profile["user_id"] = raw_data.get("id", "")

    return profile
