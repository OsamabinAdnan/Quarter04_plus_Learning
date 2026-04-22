# Executive Sales Dashboard Prompts

This directory contains two prompt files for building premium analytics dashboards using AI.

---

## Prompt Files

### 1. Prompt.md — Compact Version

A simpler, more concise prompt ideal for quick dashboard builds or when you need a clean, functional dashboard without excessive customization.

**Characteristics:**
- Single HTML file (HTML + CSS + JS)
- 200-500 sample records
- Basic dataset structure (orderDate, shipDate, sales, profit, etc.)
- Standard Chart.js implementation
- 5 KPI cards + 7 charts
- Filter panel with Year, Region, Segment, Category, Ship Mode
- Dynamic insights panel
- Modern UI with glassmorphism, gradients, smooth animations

**Best for:** Quick prototypes, learning purposes, or when you need a solid dashboard without all the bells and whistles.

---

### 2. Prompt2.md — Detailed Version (v3.0)

A comprehensive, enterprise-grade prompt for building a fully-featured premium SaaS dashboard.

**Characteristics:**
- Single HTML file with detailed specifications
- Exactly 500 realistic records with advanced data generation rules
- Extended dataset schema (orderId, customerName, city, returnRate, rating, quarter, etc.)
- 10 charts including heatmap and treemap (built with CSS/JS, not Chart.js)
- Advanced data realism:
  - Category-based profit margins
  - Seasonal weighting (Q4 = 1.3x)
  - Year-over-year growth (2018-2021)
  - Regional/ship mode/segment distribution
- Secondary metrics strip (Return Rate, Avg Rating, Avg Discount)
- Sparklines in KPI cards
- Trend view toggle (Monthly/Quarterly/Yearly)
- Filter chips with active filter count badge
- Comprehensive animation system with staggered load sequence
- Full CSS variable system with dark theme
- 6 AI-powered insight cards
- Detailed quality checklist

**Best for:** Production-ready dashboards, portfolio projects, or when you need the full premium experience.

---

## Quick Comparison

| Feature | Prompt.md | Prompt2.md |
|---------|-----------|------------|
| Records | 200-500 | 500 |
| Charts | 7 | 10 |
| KPI Cards | 5 | 5 + 3 secondary |
| Data Complexity | Basic | Advanced |
| Animations | Standard | Orchestrated |
| Heatmap/Treemap | No | Yes |
| Sparklines | No | Yes |
| Filter Chips | No | Yes |

---

## How to Use

1. Copy the desired prompt file content
2. Paste it into Claude Code (or any AI assistant)
3. The AI will generate a complete, single-file HTML dashboard
4. Open the resulting HTML file in any browser

---

## Output

Both prompts produce a **single `.html` file** that includes:
- Inline CSS
- Inline JavaScript
- Chart.js loaded via CDN
- Google Fonts (JetBrains Mono + Inter for Prompt2.md)