# 📈 Trading Wiz — Project Brain

## Identity
You are the Von Empire OS acting on the **Trading Wiz** project — options trading platform focused on LEAPS for wealth building and credit spreads for income.

## Primary Strategy: LEAPS
- **Definition:** Long-term Equity AnticiPation Securities — call/put options 12-24 months out, deep ITM (delta > 0.80)
- **Why:** Control 100 shares at fraction of cost, defined max loss, unlimited upside, stock replacement
- **Selection criteria:**
  - Delta ≥ 0.80 (mimics stock movement)
  - 12-24 months to expiration
  - Low IV rank at purchase (avoid buying expensive premiums)
  - Underlying: strong fundamental thesis, not a meme

### LEAPS Thesis: EYL (Primary)
- **Source:** InvestAnswers (James Altucher methodology)
- **Setup:** Deep ITM call, 12-18 months out, at the first support level pullback
- **Entry:** Wait for price to reach support zone, buy LEAPS at 80+ delta
- **Exit target:** 50-100%+ return on premium, or roll at 6 months DTE
- **Stop loss:** 50% loss on premium = exit and reassess

## Secondary Strategy: Income Generation
### Iron Condors
- Sell OTM call credit spread + sell OTM put credit spread
- Collect premium from both sides
- **Target:** $1-$3 per contract, 30-45 DTE
- **Management:** Close at 50% profit or 21 DTE, whichever comes first
- **Risk:** Defined max loss = width of wider spread minus premium received

### Bull Put Spreads
- Sell OTM put + buy further OTM put as protection
- Bullish or neutral outlook
- Best deployed on confirmed support bounces
- Same management: 50% profit close

### Bear Call Spreads
- Sell OTM call + buy further OTM call as protection
- Bearish or neutral outlook
- Best deployed on confirmed resistance rejections

### Diagonal Calendar Spreads (Advanced — Month 6+)
- Sell short-term calls against long-term LEAPS calls
- Generate income on existing positions
- Maintain upside exposure while collecting theta

## Current Status
- **Level 3 Exam:** In preparation
- **Study app:** ✅ Built (30 quiz questions, 9 strategy cards, P&L calculator, 30 flashcards)
- **Paper trading:** Not yet started
- **First live trade:** Pending Level 3 approval

## Platform Requirements (Being Built)
- [x] Study app (GitHub Pages)
- [ ] Live market data dashboard
- [ ] LEAPS screener with delta, DTE, IV filters
- [ ] Watchlist tracking (EYL + other candidates)
- [ ] Portfolio tracker with P&L visualization
- [ ] Options chain viewer
- [ ] Alert system (price targets, IV changes, DTE countdown)
- [ ] Trade log with automated entry/exit recording
- [ ] Weekly review auto-generated reports

## Risk Management
1. Max 2% of trading capital per trade
2. Never hold earnings through — close or reduce before
3. Paper trade 30 days minimum before live
4. All positions documented in trade log
5. Weekly position review (never "set and forget")
6. LEAPS stop: 50% premium loss = exit + reassess
7. Max single underlying: 20% of portfolio value
8. 6-month emergency fund separate from trading capital

## Resources
- **InvestAnswers YouTube** — Primary thesis generation
- **Robinhood Level 3** — Platform for execution
- **Study app** — github.com/Von-ops/Velma-Dinkly/study-guide
- **Trading Journal** — outputs/trading-wiz/trade-log.md
