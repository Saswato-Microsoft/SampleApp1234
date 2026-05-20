"""Notification service that sends personalized messages to users."""

from user_profile_parser import parse_user_profile


def send_welcome_notification(raw_user_data):
    """Send a personalized welcome notification to a new user.
    
    Bug: Directly accesses profile['first_name'] without checking
    if it exists. When user signed up via OAuth (only 'name' field
    in raw data), parse_user_profile does not include 'first_name',
    causing KeyError here.
    """
    profile = parse_user_profile(raw_user_data)

    # Bug: assumes 'first_name' always exists in parsed profile
    greeting = f"Welcome, {profile['first_name']}! Thanks for joining us."
    
    notification = {
        "to": profile["email"],
        "subject": "Welcome aboard!",
        "body": greeting,
        "user_id": profile["user_id"],
    }

    return notification


if __name__ == "__main__":
    # This triggers the bug: OAuth user has 'name' but no 'first_name'/'last_name'
    oauth_user = {
        "id": "usr_9a3f7c",
        "name": "Shreyas Waikar",
        "email": "shreyas@example.com",
        "auth_provider": "google",
    }

    result = send_welcome_notification(oauth_user)
    print(result)
