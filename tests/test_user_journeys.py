import os, requests
BASE = os.getenv("BASE_URL", "http://127.0.0.1:8000").rstrip("/")

def test_service_is_reachable():
    assert requests.get(f"{BASE}/health", timeout=10).status_code == 200

def test_project_list_journey_entrypoint():
    r = requests.get(f"{BASE}/projects", timeout=10)
    assert r.status_code == 200
    assert isinstance(r.json(), (list, dict))

# Gaps: register -> login -> create project -> create task -> update task
# -> verify ownership -> logout; cancellation and recovery journeys.
