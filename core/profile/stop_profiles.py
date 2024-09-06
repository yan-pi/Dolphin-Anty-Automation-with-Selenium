from core.browser.close_browsers import close_browsers
from core.browser.list_browsers import list_browsers
from core.browser.update_profile_status import update_profile_status
from core.browser.delete_profiles import delete_profiles
import time

def stop_profiles(drivers, auth_token):
    print("Fechando navegadores e excluindo perfis...")
    close_browsers(drivers)
    time.sleep(5)
    
    profiles_response = list_browsers(auth_token)
    profiles = profiles_response.get('data', [])
    
    for profile in profiles:
        profile_id = profile['id']
        
        if profile.get('running', False):
            print(f"Perfil {profile_id} ainda está marcado como em execução. Tentando atualizar o status...")
            try:
                update_profile_status(profile_id, auth_token, running=False)
                time.sleep(2)
            except Exception as e:
                print(f"Erro ao atualizar o status do perfil {profile_id}: {e}")
        
        try:
            delete_profiles(profile_id, auth_token)
            print(f"Perfil {profile_id} excluído com sucesso.")
        except Exception as e:
            print(f"Erro ao excluir perfil {profile_id}: {e}")