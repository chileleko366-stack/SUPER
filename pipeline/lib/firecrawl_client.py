"""Thin Firecrawl REST client. No official MCP tool exists for this
environment (see docs/RESEARCH_BRIEF.md) so this project calls the REST
API directly, same convention used by every research agent."""
import os
import requests

BASE_URL = "https://api.firecrawl.dev/v1"


def _key() -> str:
    key = os.environ.get("FIRECRAWL_API_KEY")
    if not key:
        raise RuntimeError("FIRECRAWL_API_KEY not set in environment")
    return key


def search(query: str, limit: int = 5) -> list[dict]:
    resp = requests.post(
        f"{BASE_URL}/search",
        headers={"Authorization": f"Bearer {_key()}", "Content-Type": "application/json"},
        json={"query": query, "limit": limit},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    if not data.get("success"):
        raise RuntimeError(f"Firecrawl search failed: {data}")
    return data["data"]


def scrape(url: str) -> str:
    resp = requests.post(
        f"{BASE_URL}/scrape",
        headers={"Authorization": f"Bearer {_key()}", "Content-Type": "application/json"},
        json={"url": url, "formats": ["markdown"], "onlyMainContent": True},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    if not data.get("success"):
        raise RuntimeError(f"Firecrawl scrape failed: {data}")
    return data["data"]["markdown"]
