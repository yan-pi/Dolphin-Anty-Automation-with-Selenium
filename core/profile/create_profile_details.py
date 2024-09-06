def create_profile_details(proxy_details, index):
    return {
        "name": f"browser_{index+1}",
        "tags": ["rise_extension-profiles"],
        "mainWebsite": "",
        "notes": {
            "content": None
        },
        "proxy": proxy_details
    }