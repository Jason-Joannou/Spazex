import requests
import pytest

BASE_URL = "http://127.0.0.1:8080"

@pytest.fixture(scope="module")
def new_spaza_data():
    return {
        "spaza_name": "NewUserTest",
        "spaza_reg_no": "123456",
        "spaza_email": "newusertest@example.com",
        "spaza_password": "NewUserPass1"
    }

def test_spaza_registration(new_spaza_data):
    response = requests.post(f"{BASE_URL}/register_spaza", json=new_spaza_data)
    assert response.status_code == 200, response.text
    assert response.json().get("message") == "Shop registered successfully"

if __name__ == "__main__":
    pytest.main()
