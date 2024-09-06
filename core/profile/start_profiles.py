from core.proxy.proxy_manager import validate_proxies, parse_proxy, create_proxy_details
from core.browser.list_and_open_profiles import list_and_open_profiles
from core.profile.create_profile_details import create_profile_details
from core.browser.create_profiles_in_bulk import create_profiles_in_bulk

def start_profiles(num_profiles, proxies, auth_token):
    if not validate_proxies(proxies, num_profiles):
        return []

    profiles = []
    for i in range(num_profiles):
        proxy_parts = parse_proxy(proxies[i])
        if proxy_parts is None:
            return []

        proxy_details = create_proxy_details(proxy_parts, i)
        profile = create_profile_details(proxy_details, i)
        profiles.append(profile)

    create_profiles_in_bulk(profiles, auth_token)
    print("Sucesso", "Perfis criados com sucesso.")
    
    print("Abrindo perfis criados...")
    return list_and_open_profiles(auth_token)