def close_browsers(drivers):
    for index, driver in enumerate(drivers):
        try:
            driver.quit()
            print(f"Navegador {index+1} fechado com sucesso.")
        except Exception as e:
            print(f"Erro ao fechar navegador {index+1}: {e}")
        finally:
            # Garantir que o driver seja marcado como None, mesmo se houver uma exceção
            drivers[index] = None
    
    # Limpar a lista de drivers
    while None in drivers:
        drivers.remove(None)