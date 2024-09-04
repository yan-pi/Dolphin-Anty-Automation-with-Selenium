from create_profile import create_profiles_in_bulk
from open_profile import open_profile
from delete_browsers import list_browsers, delete_browser, update_profile_status, close_browsers
import time

def list_and_open_profiles():
    profiles_response = list_browsers()
    profiles = profiles_response.get('data', [])
    
    opened_drivers = []
    for index, profile in enumerate(profiles):
        profile_id = profile['id']
        print(f"Abrindo perfil {profile_id}...")
        
        try:
            driver = open_profile(profile_id)
            if driver:
                opened_drivers.append(driver)
                x_offset = (index % 3) * 400
                y_offset = (index // 3) * 400
                driver.set_window_position(x_offset, y_offset)
            
            time.sleep(1)
        except Exception as e:
            print(f"Erro ao iniciar o perfil {profile_id}: {e}")
            continue

    return opened_drivers