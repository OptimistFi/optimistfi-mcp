"""Fails when this listing no longer matches the live server or the official MCP Registry.

Checks, each read live:
  1. the README tools table (between the tools:start and tools:end markers) against the server's tools/list,
     by name and title;
  2. server.json against the registry's latest published entry for the same name (version, description, remotes).
Stdlib only. Run: python .github/scripts/check_listing.py
"""
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

ENDPOINT = "https://mcp.optimistfi.com/mcp"
REGISTRY = "https://registry.modelcontextprotocol.io/v0/servers"


def live_tools():
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}).encode()
    req = urllib.request.Request(ENDPOINT, body, {"content-type": "application/json",
                                                  "accept": "application/json, text/event-stream",
                                                  "user-agent": "optimistfi-listing-check"})
    text = urllib.request.urlopen(req, timeout=60).read().decode()
    data = [line[5:] for line in text.splitlines() if line.startswith("data:")]
    tools = json.loads(data[-1] if data else text)["result"]["tools"]
    return {t["name"]: (t.get("title") or (t.get("annotations") or {}).get("title") or "").strip() for t in tools}


def readme_tools():
    readme = open("README.md", encoding="utf-8").read()
    block = readme.split("<!-- tools:start", 1)[1].split("<!-- tools:end -->", 1)[0]
    rows = re.findall(r"^\|\s*`([a-z_]+)`\s*\|\s*([^|]+?)\s*\|", block, flags=re.M)
    return dict(rows)


def registry_entry(name):
    url = f"{REGISTRY}/{urllib.parse.quote(name, safe='')}/versions/latest"
    try:
        return json.loads(urllib.request.urlopen(url, timeout=60).read())["server"]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def main():
    problems = []
    live, listed = live_tools(), readme_tools()
    for name in sorted(set(live) - set(listed)):
        problems.append(f"README is missing the live tool `{name}` ({live[name]})")
    for name in sorted(set(listed) - set(live)):
        problems.append(f"README lists `{name}`, which the live server no longer serves")
    for name in sorted(set(live) & set(listed)):
        if live[name] != listed[name]:
            problems.append(f"`{name}` is titled '{live[name]}' on the server and '{listed[name]}' in the README")

    local = json.load(open("server.json", encoding="utf-8"))
    published = registry_entry(local["name"])
    if not published:
        problems.append(f"the registry has no active latest entry named {local['name']}")
    else:
        for key in ("version", "description", "remotes", "websiteUrl"):
            if published.get(key) != local.get(key):
                problems.append(f"server.json {key} differs from the registry: {local.get(key)!r} here, {published.get(key)!r} published")

    if problems:
        print("The public listing is out of date:\n- " + "\n- ".join(problems))
        print("\nUpdate README.md and server.json here, then publish server.json to the MCP Registry with a new version.")
        sys.exit(1)
    print(f"ok: {len(live)} tools match the live server; server.json matches registry version {local['version']}")


if __name__ == "__main__":
    main()
