from settings import settings


class TestHealth:
    def test_health(self, client) -> None:
        response = client.get(
            f"{settings.api_prefix}/health",
        )
        assert response.status_code == 200
        content = response.json()
        assert "status" in content
