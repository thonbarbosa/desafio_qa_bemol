import pip._vendor.requests as requests
import unittest

BASE_URL = "https://serverest.dev"

class ServerestTest(unittest.TestCase):

    def setUp(self):
        self.headers = {'Content-Type': 'application/json'}
        self.user_data = {
            "nome": "Orlithon",
            "email": "orlithon.teste@exemplo.com",
            "password": "123456",
            "administrador": "true"
        }
        self.login_data = {
            "email": self.user_data['email'],
            "password": self.user_data['password']
        }
        self.product_data = {
            "nome": "Produto Teste",
            "preco": 100,
            "descricao": "Descrição do produto",
            "quantidade": 10
        }
        self.user_id = None
        self.token = None
        self.product_id = None

    def test_01_create_user(self):
        # Criação do usuário
        response = requests.post(f"{BASE_URL}/usuarios", json=self.user_data, headers=self.headers)
        print(f"Resposta da criação do usuário: {response.json()}")
        self.assertEqual(response.status_code, 201)
        self.user_id = response.json().get('_id')
        print(f"Usuário criado com ID: {self.user_id}")
        
        # Login para obter token
        login_response = requests.post(f"{BASE_URL}/login", json=self.login_data, headers=self.headers)
        print(f"Resposta do login: {login_response.json()}")
        self.assertEqual(login_response.status_code, 200)
        self.token = login_response.json().get('authorization')
        print(f"Token obtido: {self.token}")
        
        # Atualiza os headers para incluir o token de autenticação
        self.headers['Authorization'] = f"Bearer {self.token}"

    def test_02_verify_user_creation(self):
        # Verifica se o usuário foi criado com sucesso
        print(f"Verificando usuário com ID: {self.user_id}")
        response = requests.get(f"{BASE_URL}/usuarios/{self.user_id}", headers=self.headers)
        print(f"Resposta da verificação do usuário: {response.json()}")
        self.assertEqual(response.status_code, 200)
        user = response.json()
        self.assertEqual(user['nome'], self.user_data['nome'])
        self.assertEqual(user['email'], self.user_data['email'])
        print("Verificação de usuário criada com sucesso.")

    def test_03_create_product(self):
        # Criação do produto com autenticação
        print("Criando produto...")
        response = requests.post(f"{BASE_URL}/produtos", json=self.product_data, headers=self.headers)
        print(f"Resposta da criação do produto: {response.json()}")
        self.assertEqual(response.status_code, 201)
        self.product_id = response.json().get('_id')
        print(f"Produto criado com ID: {self.product_id}")

    def test_04_verify_product_creation(self):
        # Verificação da criação do produto
        print(f"Verificando produto com ID: {self.product_id}")
        response = requests.get(f"{BASE_URL}/produtos/{self.product_id}", headers=self.headers)
        print(f"Resposta da verificação do produto: {response.json()}")
        self.assertEqual(response.status_code, 200)
        product = response.json()
        self.assertEqual(product['nome'], self.product_data['nome'])
        self.assertEqual(product['preco'], self.product_data['preco'])
        print("Verificação de produto criada com sucesso.")

if __name__ == '__main__':
    unittest.main()

