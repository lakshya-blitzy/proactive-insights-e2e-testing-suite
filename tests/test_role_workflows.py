import os, requests
BASE = os.getenv("BASE_URL", "http://127.0.0.1:8000").rstrip("/")

def test_team_endpoint_handles_anonymous_user():
    r = requests.get(f"{BASE}/teams", timeout=10)
    assert r.status_code in (200, 401, 403, 404)

# Gaps: admin/member permissions, cross-user access, invitations,
# revoked sessions and stale-token behaviour.
