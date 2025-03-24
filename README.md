# ctf-mcp-server


先临时搞几个先

```json
{
  "mcpServers": {
    "ctftools": {
      "command": "python",
      "args": [
        "D:\\xxx\\server.py"
      ],
      "alwaysAllow": [
        "decode_qr",
        "create_qr",
        "b64_encode",
        "b64_decode",
        "b58_encode",
        "b58_decode"
      ],
      "timeout": 900
    }
  }
}
```
