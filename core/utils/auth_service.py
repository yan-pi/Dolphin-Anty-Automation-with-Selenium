# utils/auth_service.py
import requests

class AuthService:
    def __init__(self):
        self.base_url = "https://resolute.fun/api/logar3.php"

    def login(self, username, password):
        # Concatenar o username e password na URL
        url = f"{self.base_url}?username={username}&password={password}"
        
        # Cabeçalhos personalizados
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        try:
            # Fazendo a requisição GET com a URL concatenada
            response = requests.get(url, headers=headers)

            # Verifica se o status code é 200
            if response.status_code == 200:
                try:
                    # Tenta converter a resposta em JSON
                    data = response.json()

                    # Verifica se a autenticação foi bem-sucedida
                    if data.get("success"):
                        return True, "Login bem-sucedido"
                    else:
                        return False, data.get("message", "Falha na autenticação")
                except ValueError:
                    # Erro ao decodificar a resposta como JSON
                    return False, "Erro ao processar a resposta JSON do servidor."
            else:
                # Status code diferente de 200
                return False, f"Falha na autenticação. Status code: {response.status_code}"
        
        except requests.RequestException as e:
            # Tratamento de exceção de conexão
            return False, f"Erro de conexão: {str(e)}"

