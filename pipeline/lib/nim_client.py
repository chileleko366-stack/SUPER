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


def generate_json(system_prompt: str, user_prompt: str, max_tokens: int = 900, retries: int = 2, temperature: float = 0.7) -> dict:
    """Calls NIM chat completions and parses the reply as JSON, tolerating
    markdown code fences since instruction-following on this isn't perfect.
    Retries the call itself (not just JSON extraction) on a parse failure --
    at temperature 0.7 a malformed/truncated reply is often just a bad
    sample, not a deterministic failure, and simply reusing the same
    unparseable text would fail again."""
    last_error = None
    for attempt in range(retries + 1):
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
                "temperature": temperature,
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
                last_error = RuntimeError(f"NIM response did not contain JSON: {content[:400]}")
                continue
            raw = raw[brace:]
        try:
            return json.loads(raw)
        except json.JSONDecodeError as e:
            last_error = RuntimeError(f"NIM response was not valid JSON ({e}): {content[:400]}")
    raise last_error
