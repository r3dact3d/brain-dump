---
type: ai-note
description: This is my ai template
---


# quantization

## Context quantization

> Conversation History

OLLAMA_FLASH_ATTENTION=true
OLLAMA_KV_CACHE_TYPE=f16

```bash
ollama run qwen2.5
>>> /set parameter num_ctx 32678
>>> /save qwen2.5max
>>> /bye 
```

Start with a Q4 model 
Enable Flash OLLAMA_FLASH_ATTENTION
Test your Use Case
OK? Try Q2 or Q3
