from app import app


def test_healthz():
    client = app.test_client()
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_products_api():
    client = app.test_client()
    response = client.get("/api/products")
    assert response.status_code == 200
    products = response.get_json()
    assert isinstance(products, list)
    assert len(products) >= 1
