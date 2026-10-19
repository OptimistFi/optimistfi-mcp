# OptimistFi MCP Server

Market data and research for AI assistants: perpetual futures across 40 venues, the rules and pricing of 21 perps prop firms, and dated investment theses on more than 6,100 US equities.

```
https://mcp.optimistfi.com/mcp
```

Remote server over Streamable HTTP. Read-only. No API key or account required.

## Coverage

**Perpetual futures.** Forty venues, including Hyperliquid and its builder markets, Lighter, Aster, dYdX, Paradex, gTrade, Ostium, Vest, Orderly, Kraken Futures, OKX and Bitget: approximately 1,560 assets and 9,400 markets across crypto, equity, index, commodity and FX perpetuals. For each market: funding on every venue, open interest, maximum leverage, liquidation levels from live Hyperliquid positions, large trades, order-book depth and the net positioning of Hyperliquid's largest accounts, with up to 90 days of history. Market-wide: cross-venue funding spreads, movers, liquidations, new listings and multi-day position builds.

**Perps prop firms.** Rules, account sizes and challenge pricing for 21 firms, sourced from each firm's published terms, with current discount codes and net pricing.

**US equities.** A dated investment thesis for more than 6,100 companies, with testable claims, the condition that would invalidate each, and an assessment against the latest filings. Supported by SEC filings, insider and congressional transactions, capital returns and the earnings calendar.

Every response is timestamped and attributed to its source.

## Connect

**Claude:** available in [Claude's connectors directory](https://claude.ai/directory/mcp-optimistfi-com).

**Claude Code**

```bash
claude mcp add --transport http optimistfi https://mcp.optimistfi.com/mcp
```

**Cursor:** install this repository as a plugin, or add to `.cursor/mcp.json`:

```json
{ "mcpServers": { "optimistfi": { "url": "https://mcp.optimistfi.com/mcp" } } }
```

**VS Code:** add to `.vscode/mcp.json`:

```json
{ "servers": { "optimistfi": { "type": "http", "url": "https://mcp.optimistfi.com/mcp" } } }
```

**ChatGPT and other clients:** add `https://mcp.optimistfi.com/mcp` as a remote MCP server.

Setup guides for each client: [optimistfi.com/mcp/docs/clients](https://optimistfi.com/mcp/docs/clients)

## Tools

<!-- tools:start -->
| Tool | Title | Description |
|---|---|---|
| `get_perps` | Perpetual futures | A single market across venues: price and premium to the index or underlying equity, open interest, funding, maximum leverage, liquidation levels, large trades and positioning |
| `get_perps_market` | Perpetual futures — whole market | The full market across approximately 1,600 assets: funding and cross-venue spreads, movers, open interest, liquidations, large trades, new listings, weekend pricing, large-account positioning, leverage and position builds |
| `get_perps_history` | Perpetual futures — history | A single market over 1 to 90 days: price, open interest, funding, taker flow, large-account net positioning and order-book depth |
| `get_perps_desk` | Perps desk — news, traders and wallets | Published perps coverage with sources, tracked traders and the record of their calls, and covered Hyperliquid wallets |
| `get_prop_firms` | Prop firms for perpetual futures | Perps prop firm rules, challenge pricing net of current codes, discount codes, jurisdictions, platforms, assets and maximum allocation |
| `answer` | Financial answer | A complete read on a stock: the investment case, valuation from filed financials, and the latest quarter |
| `get_thesis` | Investment thesis | The investment case: testable claims, the condition that would invalidate each, the bear case, catalysts and current standing |
| `get_thesis_impact` | Thesis impact of an event | A metric's recent quarters assessed against the investment case |
| `what_changed` | What changed recently | Developments since a given date, assessed against the investment case: earnings, filings, insider activity, capital returns and price |
| `get_track_record` | Track record | A dated record of each filing that met or held a thesis's invalidation condition |
| `compare` | Compare companies | Two or more companies compared on valuation and investment case |
| `resolve_entity` | Resolve a company or ticker | Resolves a ticker, name or CIK to the canonical company |
| `get_filings` | SEC filings & events | 8-K events, press releases, filing text and governance flags |
| `get_calendar` | Upcoming dated events | Upcoming earnings, projected from the company's filing history, and clinical trial readouts |
| `get_capital_returns` | Dividends & buybacks | Dividend history, buyback authorizations against capital deployed, and splits |
| `get_insider_trades` | Insider transactions | Form 4 transactions: insider, role, transaction type, shares and value |
| `get_congress_trades` | Congressional trades | US House disclosures under the STOCK Act, by ticker or by member |
<!-- tools:end -->

Parameters and response formats: [optimistfi.com/mcp/docs](https://optimistfi.com/mcp/docs)

## Example queries

- Which venues offer BTC at 50x leverage, and where is liquidation?
- How much BTC would be liquidated on a 5% decline, and where are the clusters?
- How are Hyperliquid accounts above $1M positioned on BTC, ETH and HYPE?
- Where is BTC funding lowest for a long position across venues?
- Which perps prop firms offer a $50K challenge, and what is the net price after current codes?
- Does the NVIDIA investment thesis hold after the latest 10-Q?

## Registry

Official MCP Registry: `com.optimistfi/optimistfi` ([server.json](server.json))

## Legal

OptimistFi provides market data and research. The service does not execute transactions or provide personalized investment advice. See the [methodology](https://optimistfi.com/methodology), [disclosures](https://optimistfi.com/disclosures) and [terms](https://optimistfi.com/terms).

Contact: hello@optimistfi.com
