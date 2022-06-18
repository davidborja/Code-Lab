def test_service_shopping_with_parameter(client):
    """
    test service get statistics
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    data = "test"
    url = f"/api/v1/shopping/statistics?category={data}"
    response = client.get(url, headers=headers)
    print(response.data)
    print(response.status)
    assert response.status == "200 OK"


def test_service_shopping_without_parameter(client):
    """
    test service get statistics
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    url = "/api/v1/shopping/statistics"
    response = client.get(url, headers=headers)
    print(response.data)
    print(response.status)
    assert response.status == "200 OK"


def test_service_shopping_bad_parameters(client):
    """
    test service get statistics bad parameters
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    data = "test"
    url = f"/api/v1/shopping/statistics?categor={data}"
    response = client.get(url, headers=headers)
    print(response.data)
    print(response.status)
    assert response.status == "400 BAD REQUEST"
