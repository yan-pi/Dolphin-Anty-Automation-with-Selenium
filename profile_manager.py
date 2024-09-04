from proxy_manager import validate_proxies, parse_proxy, create_proxy_details
from browser_manager import create_profiles_in_bulk, list_and_open_profiles, close_browsers, list_browsers, delete_browser, update_profile_status
import time

def start_profiles(num_profiles, proxies):
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

    create_profiles_in_bulk(profiles)
    print("Sucesso", "Perfis criados com sucesso.")
    
    print("Abrindo perfis criados...")
    return list_and_open_profiles()

def stop_profiles(drivers):
    print("Fechando navegadores e excluindo perfis...")

    close_browsers(drivers)

    time.sleep(5)

    profiles_response = list_browsers()
    profiles = profiles_response.get('data', [])
    
    for profile in profiles:
        profile_id = profile['id']
        
        if profile.get('running', False):
            print(f"Perfil {profile_id} ainda está marcado como em execução. Tentando atualizar o status...")
            try:
                update_profile_status(profile_id, running=False)
                time.sleep(2)
            except Exception as e:
                print(f"Erro ao atualizar o status do perfil {profile_id}: {e}")
        
        try:
            delete_browser(profile_id)
            print(f"Perfil {profile_id} excluído com sucesso.")
        except Exception as e:
            print(f"Erro ao excluir perfil {profile_id}: {e}")

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