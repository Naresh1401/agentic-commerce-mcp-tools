from fastapi.testclient import TestClient
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'mcp-server'))
from server import app

client = TestClient(app)

def test_list_tools():
    response = client.get('/tools/list')
    assert response.status_code == 200
    names = {tool['name'] for tool in response.json()['tools']}
    assert {'search_products', 'create_checkout_session'} <= names

def test_partner_agent_blocked_from_cart_update():
    response = client.post('/tools/call', json={'tool': 'update_cart', 'role': 'partner_agent', 'input': {'cart_id': 'cart_123', 'sku': 'SKU-PASTA-001', 'quantity': 1, 'action': 'add'}})
    assert response.status_code == 403

