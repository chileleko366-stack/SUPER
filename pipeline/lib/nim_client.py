"""NVIDIA NIM (cloud LLM API) client for script generation."""
import json
import os
import re
import requests

BASE_URL = "https://integrate.api.nvidia.com/v1"
MODEL = "meta/llama-3.1-8b-instruct"


def _key() -> str:
    key = os.environ.get("NVIDIA_NIM_API_KEY")
    if not key:
        raise RuntimeError("NVIDIA_NIM_API_KEY not set in environment")
    return key


def generate_json(system_prompt: str, user_prompt: str, max_tokens: int = 900) -> dict:
    """Calls NIM chat completions and parses the reply as JSON, tolerating
    markdown code fences since instruction-following on this isn't perfect."""
    resp = requests.post(
        f"{BASE_URL}/chat/completions",
        headers={"Authorization": f"Bearer {_key()}", "Content-Type": "application/json"},
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "max_tokens": max_tokens,
            "temperature": 0.7,
        },
        timeout=60,
    )
    resp.raise_for_status()
    data = resp.json()
    content = data["choices"][0]["message"]["content"]

    fenced = re.search(r"```(?:json)?\s*(\{.*\})\s*```", content, re.DOTALL)
    raw = fenced.group(1) if fenced else content
    raw = raw.strip()
    if not raw.startswith("{"):
        brace = raw.find("{")
        if brace == -1:
            raise RuntimeError(f"NIM response did not contain JSON: {content[:400]}")
        raw = raw[brace:]
    return json.loads(raw)
