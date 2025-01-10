python-playground
---

## in terminal
```bash
uv init aoc2024-py
uv tool install ruff


# add dependencies
uv add requests
uv add requests_mock
uv add pytest
```

## in vs code
* install microsoft python plugin
* install ruff plugin
* change settings to below

```json
{
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit"
        }
    },
    "ruff.fixAll": true,
    "ruff.organizeImports": true
}
```
