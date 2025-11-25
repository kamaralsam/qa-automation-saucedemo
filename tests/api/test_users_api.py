import requests
import requests_mock

BASE_URL = "https://reqres.in/api"

def test_get_users_list_returns_200_and_users():
    mock_data = {
        "page": 2,
        "per_page": 6,
        "total": 12,
        "total_pages": 2,
        "data": [
            {"id": 7, "email": "user7@test.com"},
            {"id": 8, "email": "user8@test.com"},
        ]
    }

    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URL}/users", json=mock_data, status_code=200)

        response = requests.get(f"{BASE_URL}/users", params={"page": 2})

        assert response.status_code == 200
        assert len(response.json()["data"]) > 0
