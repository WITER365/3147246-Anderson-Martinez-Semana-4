def test_crear_producto_sin_categoria(client):
    response = client.post("/productos/", json={
        "nombre": "Producto Test",
        "precio": 99.99,
        "descripcion": "Producto de prueba"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Producto Test"

def test_crear_producto_con_categoria(client):
    cat_resp = client.post("/categorias/", json={"nombre": "Tecnología", "descripcion": "Productos tecnológicos"})
    categoria_id = cat_resp.json()["id"]
    response = client.post("/productos/", json={
        "nombre": "Smartphone",
        "precio": 599.99,
        "descripcion": "Teléfono inteligente",
        "categoria_id": categoria_id
    })
    assert response.status_code == 200
    data = response.json()
    assert data["categoria_id"] == categoria_id

def test_listar_productos_con_categoria(client):
    cat_resp = client.post("/categorias/", json={"nombre": "Hogar", "descripcion": "Productos para el hogar"})
    categoria_id = cat_resp.json()["id"]
    client.post("/productos/", json={
        "nombre": "Aspiradora",
        "precio": 199.99,
        "descripcion": "Aspiradora potente",
        "categoria_id": categoria_id
    })
    response = client.get("/productos/")
    data = response.json()
    assert len(data) == 1
    assert data[0]["categoria"]["nombre"] == "Hogar"

def test_productos_por_categoria(client):
    cat_resp = client.post("/categorias/", json={"nombre": "Ropa", "descripcion": "Prendas de vestir"})
    categoria_id = cat_resp.json()["id"]
    client.post("/productos/", json={"nombre": "Camiseta", "precio": 25.99, "descripcion": "Camiseta algodón", "categoria_id": categoria_id})
    client.post("/productos/", json={"nombre": "Pantalón", "precio": 45.99, "descripcion": "Pantalón casual", "categoria_id": categoria_id})
    response = client.get(f"/categorias/{categoria_id}/productos/")
    data = response.json()
    assert len(data) == 2

def test_validacion_precio_negativo(client):
    response = client.post("/productos/", json={"nombre": "Producto Inválido", "precio": -10.99, "descripcion": "Precio negativo"})
    assert response.status_code == 400
