# MCP Tools

This repo includes a lightweight MCP-style JSON server at `mcp-server/server.py`. It is not claiming official MCP certification; it demonstrates the interface pattern.

| Tool | Risk | Roles |
| --- | --- | --- |
| search_products | read-only | customer, associate, admin, partner_agent |
| check_inventory | read-only | customer, associate, admin, partner_agent |
| get_price | read-only | customer, associate, admin, partner_agent |
| apply_coupon | cart-modifying | customer, admin |
| update_cart | cart-modifying | customer, admin |
| create_checkout_session | checkout/payment-sensitive | customer, admin |
| track_order | read-only | customer, associate, admin |

Example:

```json
{{
  "tool": "search_products",
  "input": {{"query": "organic milk", "category": "dairy", "max_results": 5}},
  "role": "customer"
}}
```
