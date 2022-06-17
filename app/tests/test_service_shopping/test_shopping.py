def test_service_shopping(client):
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
