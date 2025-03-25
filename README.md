# CTF-MCP-Server

  尝试用AI进行CTF解题

## 两种服务器

1. **ctftools_Puzzle_server**：主要用于解题
2. **ctftools_feces_making_machine_server**：主要用于出题

## 使用方法

 使用Cline 或者二开相关插件，导入mcp配置文件





```json
{
  "mcpServers": {
    "ctftools_Puzzle_server": {
      "command": "python",
      "args": [
        "D:\\AI\\ctf-mcp-server\\ctftools_Puzzle_server.py"
      ],
      "timeout": 1800
    },
    "ctftools_feces_making_machine_server": {
      "command": "python",
      "args": [
        "D:\\AI\\ctf-mcp-server\\ctftools_feces_making_machine_server.py"
      ],
      "timeout": 1800
    }
  }
}
```
