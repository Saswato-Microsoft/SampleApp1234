"""Configuration loader for the batch processing system."""

APP_DEFAULTS = {
    "app_name": "sampleapp1234",
    "max_retries": 3,
    "timeout_seconds": 30,
}


def load_batch_config(config_dict=None):
    """Load batch processing configuration.
    
    Bug: Returns batch_size=0 when the key is missing from config,
    instead of raising an error or using a safe default like 1.
    """
    if config_dict is None:
        config_dict = {}

    return {
        "batch_size": config_dict.get("batch_size", 0),  # Bug: defaults to 0 instead of safe value
        "max_retries": config_dict.get("max_retries", APP_DEFAULTS["max_retries"]),
        "timeout": config_dict.get("timeout", APP_DEFAULTS["timeout_seconds"]),
    }
