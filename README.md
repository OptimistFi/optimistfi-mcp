# OptimistFi MCP server

Live perpetual futures data on 40 venues, the rules and prices of 21 perps prop firms, and sourced investment theses on 6,100+ US stocks, for Claude, ChatGPT, Cursor and any MCP client.

```
https://mcp.optimistfi.com/mcp
```

Public and read-only. No API key, no sign-up. Streamable HTTP.

This repository is the public listing of a hosted server: how to connect, what each tool answers, and the manifests that directories and editors read. The server itself runs at the endpoint above; its code is not in this repository.

## What it covers

**Perpetual futures, 40 venues.** Hyperliquid and its builder markets, Lighter, Aster, dYdX, Paradex, gTrade, Ostium, Vest, Orderly, Kraken Futures, OKX, Bitget and more: about 1,560 assets and 9,400 markets across crypto, stock, index, commodity and FX perps. For any market: funding on every venue, open interest, maximum leverage, liquidation levels from real Hyperliquid positions, whale trades, order-book depth and the net position of Hyperliquid's largest accounts, with up to 90 days of history. Across the market: funding gaps between venues, movers, liquidations, new listings, multi-day position builds and the weekend read of stock perps.

**Perps prop firms.** The rules, account sizes and challenge prices of 21 firms, read from each firm's own pages, with live discount codes and the price after the code.

**US stocks.** A dated investment thesis for more than 6,100 companies: testable claims, the condition that breaks each one, and whether the latest filings support it, with SEC filings, insider and congressional trades, capital returns and the earnings calendar behind every answer.

Every answer carries the time its data was read and the source it came from.

## Connect

**Claude** (claude.ai, Desktop, mobile): add OptimistFi from [Claude's connectors directory](https://claude.ai/directory/mcp-optimistfi-com), or add the endpoint as a custom connector.

**Claude Code**

```bash
claude mcp add --transport http optimistfi https://mcp.optimistfi.com/mcp
```

**Cursor**: install the plugin in this repository, or add to `.cursor/mcp.json`:

```json
{ "mcpServers": { "optimistfi": { "url": "https://mcp.optimistfi.com/mcp" } } }
```

**VS Code**: add to `.vscode/mcp.json`:

```json
{ "servers": { "optimistfi": { "type": "http", "url": "https://mcp.optimistfi.com/mcp" } } }
```

**ChatGPT**: add `https://mcp.optimistfi.com/mcp` as a custom connector in the app's connector settings.

**Any other client**: point it at `https://mcp.optimistfi.com/mcp` over Streamable HTTP. No `Authorization` header is needed.

Step-by-step setup for each client: [optimistfi.com/mcp/docs/clients](https://optimistfi.com/mcp/docs/clients).

## Tools

Seventeen read-only tools. Each tool's parameters and a recorded response are on its page in the [documentation](https://optimistfi.com/mcp/docs).

<!-- tools:start (checked daily against the live server by .github/workflows/listing-drift.yml) -->
| Tool | Title | What it answers |
|---|---|---|
| `get_perps` | Perpetual futures | One market right now, venue by venue: price and premium to the index or stock, open interest, funding, max leverage, liquidation levels, whale trades and positioning |
| `get_perps_market` | Perpetual futures — whole market | The whole market across about 1,600 assets: funding and funding gaps, movers, open interest, liquidations, whales, new listings, the weekend read, where big accounts lean, leverage and position builds |
| `get_perps_history` | Perpetual futures — history | One market over time (1 to 90 days): price, open interest, funding, taker buying and selling, big accounts' net position, and the latest book depth |
| `get_perps_desk` | Perps desk — news, traders and wallets | The perps desk's published stories with their sources, the traders it follows with their checked calls, and the Hyperliquid wallets it has covered |
| `get_prop_firms` | Prop firms for perpetual futures | Perps prop firms from their own pages: rules, each challenge's price after any live code, discount codes, country, platforms, assets and maximum allocation |
| `answer` | Financial answer | A stock's full read in one call: the standing investment case, valuation off its filed financials, and the latest quarter |
| `get_thesis` | Investment thesis | The standing case for a stock: its testable claims, the condition that breaks each, the bear case, catalysts and whether it still holds |
| `get_thesis_impact` | Thesis impact of an event | One metric's recent quarters read against the case: the claim it tests and whether it supports or challenges it |
| `what_changed` | What changed recently | What has happened for a company since a date, read against its case: earnings, filings, insider trades, capital returns and the price move |
| `get_track_record` | Track record | The dated record of each time a filing crossed or held a thesis's break condition |
| `compare` | Compare companies | Two or more companies side by side on valuation and the cases they rest on |
| `resolve_entity` | Resolve a company or ticker | A ticker, name or CIK resolved to the canonical company before other tools run |
| `get_filings` | SEC filings & events | A company's 8-K events, press releases, filing text and governance red flags |
| `get_calendar` | Upcoming dated events | What is ahead for a company: the next earnings date from its own filing cadence, and trial readouts |
| `get_capital_returns` | Dividends & buybacks | Dividend history with each raise or cut, buyback authorizations beside the cash actually spent, and splits |
| `get_insider_trades` | Insider transactions | Form 4 insider transactions, newest first: who, role, transaction code, shares and value |
| `get_congress_trades` | Congressional trades | US House stock-trade disclosures by ticker or by member, dated by transaction |
<!-- tools:end -->

## Questions it answers

- Which venues let me trade BTC at 50x, and how far away is liquidation?
- How much BTC gets liquidated if the price falls 5%, and where are the clusters?
- Which way are Hyperliquid's $1M+ accounts leaning on BTC, ETH and HYPE?
- Where is BTC funding cheapest to go long, and which venue pays shorts the most?
- Which perps prop firms sell a $50K challenge, and what does each cost after its discount code?
- Does the NVIDIA thesis still hold after the latest 10-Q?

## Listings

- Official MCP Registry: `com.optimistfi/optimistfi` ([server.json](server.json))
- [Claude connectors directory](https://claude.ai/directory/mcp-optimistfi-com)
- [Glama](https://glama.ai/mcp/connectors/com.optimistfi.mcp/optimist-fi)

## Terms

The server returns dated market data and sourced research. It executes no trades and gives no personalized investment advice. See the [methodology](https://optimistfi.com/methodology), [disclosures](https://optimistfi.com/disclosures) and [terms](https://optimistfi.com/terms).

Questions or a wrong number: open an issue here, or write to hello@optimistfi.com.

## Keeping this listing current

This repository mirrors the live server. A daily check ([listing-drift.yml](.github/workflows/listing-drift.yml)) compares the tools table and the `server.json` version with the server's own `tools/list` and `serverInfo`, and fails when they differ. The server's test suite fails when its public tool menu changes without the same change here.
