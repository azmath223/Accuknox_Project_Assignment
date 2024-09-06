import requests

def test_frontend_backend_integration():
    frontend_url = 'http://<http://backend-service:5000>'
    response = requests.get(frontend_url)
    
    #To Check Frontend services working or not.
    assert response.status_code == 200, "Frontend service not reachable"
    
    message = response.json().get("greeting")
    assert message == "Hello from Backend", "Greeting message mismatch"

if __name__ == "__main__":
    test_frontend_backend_integration()
