# 🚀 ELITE EXECUTIVE SALES DASHBOARD — MASTER BUILD PROMPT v3.0

You are a **world-class Frontend Engineer**, **Data Visualization Architect**, and **Product Design Lead**
with deep expertise in building enterprise-grade SaaS analytics products.

You do NOT just write code.
You craft **pixel-perfect**, **deeply interactive**, **animation-rich** dashboards that feel like
shipping products from companies like **Stripe**, **Linear**, **Vercel**, **Retool**, and **Tableau**.

Every detail matters — spacing, animation timing, color contrast, typography, micro-interactions.
If it doesn't feel **alive and premium**, improve it until it does.

---

## 🎯 OBJECTIVE

Build a **visually stunning**, **fully interactive**, **single-file HTML analytics dashboard**
that rivals premium BI tools in both aesthetics and functionality.

The output must be ONE complete `.html` file with all CSS and JavaScript inline.
No frameworks. No build tools. No external files except Chart.js CDN and Google Fonts.

---

## 📊 DATASET SPECIFICATION

Generate exactly **500 realistic records** in JavaScript using this schema:

```js
{
  orderId,        // "ORD-10001" to "ORD-10500"
  orderDate,      // "YYYY-MM-DD" between 2018–2021
  shipDate,       // 2–7 days after orderDate
  shipMode,       // "First Class" | "Second Class" | "Standard Class" | "Same Day"
  customerId,     // "CUS-0001" to "CUS-0120"
  customerName,   // realistic first + last name
  category,       // "Furniture" | "Office Supplies" | "Technology"
  subCategory,    // realistic sub based on category (see list below)
  segment,        // "Consumer" | "Corporate" | "Home Office"
  region,         // "East" | "West" | "Central" | "South"
  state,          // realistic US state name
  city,           // realistic city matching the state
  sales,          // float, 2 decimals, range: 20–2000
  profit,         // ALWAYS POSITIVE — use category margin logic below
  quantity,       // integer 1–15
  discount,       // float 0.00–0.20 (never exceeds 20%)
  returnRate,     // 0 or 1 (assign 1 to ~10% of records randomly)
  rating,         // integer 1–5 (customer satisfaction)
  year,           // 2018 | 2019 | 2020 | 2021
  month,          // 1–12
  quarter         // "Q1" | "Q2" | "Q3" | "Q4"
}
```

### Sub-Category Lists:

Furniture:       Chairs, Tables, Bookcases, Furnishings
Office Supplies: Paper, Binders, Storage, Art, Labels, Fasteners, Envelopes, Supplies, Appliances
Technology:      Phones, Accessories, Machines, Copiers

### State → City Mapping (use these pairs):

California → Los Angeles, San Francisco, San Diego
Texas → Houston, Dallas, Austin
New York → New York City, Buffalo, Albany
Florida → Miami, Orlando, Tampa
Illinois → Chicago, Springfield, Naperville
Washington → Seattle, Spokane, Tacoma
Pennsylvania → Philadelphia, Pittsburgh, Allentown
Georgia → Atlanta, Savannah, Augusta
Ohio → Columbus, Cleveland, Cincinnati
Michigan → Detroit, Grand Rapids, Lansing
Colorado → Denver, Boulder, Colorado Springs
Arizona → Phoenix, Tucson, Scottsdale
Virginia → Richmond, Arlington, Norfolk
North Carolina → Charlotte, Raleigh, Durham
Minnesota → Minneapolis, Saint Paul, Rochester
Tennessee → Nashville, Memphis, Knoxville
Maryland → Baltimore, Annapolis, Rockville
Indiana → Indianapolis, Fort Wayne, Evansville
Wisconsin → Milwaukee, Madison, Green Bay
Massachusetts → Boston, Worcester, Cambridge

### Data Realism Rules:

**Profit Formula (NEVER negative):**
```js
const categoryMargins = {
  'Technology':      { min: 0.20, max: 0.40 },
  'Office Supplies': { min: 0.15, max: 0.30 },
  'Furniture':       { min: 0.08, max: 0.18 }
};
const grossMargin = rnd(min, max);
const discountImpact = discount * rnd(0.2, 0.5); // discount only partially erodes margin
const netMargin = Math.max(0.03, grossMargin - discountImpact);
const profit = parseFloat((sales * netMargin).toFixed(2)); // always > 0
```

**Seasonal Weighting:**
- Q4 (Oct–Dec): sales multiplied by 1.3
- Q3 (Jul–Sep): multiplied by 1.1
- Q1 (Jan–Mar): multiplied by 0.85
- Q2 (Apr–Jun): baseline

**Year-over-Year Growth:**
```js
const yoyMultiplier = { 2018: 1.0, 2019: 1.12, 2020: 1.25, 2021: 1.40 };
sales = sales * yoyMultiplier[year];
```

**Regional Order Distribution:**
- West: 28%, East: 30%, Central: 22%, South: 20%

**Ship Mode Distribution:**
- Standard Class: 50%, Second Class: 25%, First Class: 18%, Same Day: 7%

**Segment Distribution:**
- Consumer: 52%, Corporate: 30%, Home Office: 18%

**Rating Logic:**
- High discount (>15%) → rating skews 3–5
- Low profit margin → rating skews 1–3
- Otherwise → rating 3–5

---

## 🎨 DESIGN SYSTEM

### Font Stack
```html
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
```
- **Headings / KPI values / Logo**: `JetBrains Mono` — monospaced, technical, bold
- **Body / labels / tooltips**: `Inter` — clean, legible, modern
- **Chart fonts**: `JetBrains Mono`

### Full CSS Variable System:
```css
:root {
  /* Backgrounds */
  --bg:         #070b12;
  --bg2:        #0c1220;
  --bg3:        #111827;
  --bg4:        #1a2235;

  /* Borders */
  --border:     rgba(255,255,255,0.07);
  --border-hi:  rgba(255,255,255,0.14);
  --border-bright: rgba(255,255,255,0.22);

  /* Text */
  --text:       #e2e8f4;
  --text-muted: #64748b;
  --text-dim:   #374151;
  --text-faint: #1f2937;

  /* Brand Colors */
  --teal:       #00d4b4;
  --blue:       #3b82f6;
  --indigo:     #6366f1;
  --purple:     #a855f7;
  --rose:       #f43f5e;
  --amber:      #f59e0b;
  --green:      #10b981;
  --orange:     #f97316;
  --cyan:       #06b6d4;
  --lime:       #84cc16;

  /* Transparent tints */
  --teal-dim:   rgba(0,212,180,0.10);
  --blue-dim:   rgba(59,130,246,0.10);
  --purple-dim: rgba(168,85,247,0.10);
  --rose-dim:   rgba(244,63,94,0.10);
  --amber-dim:  rgba(245,158,11,0.10);
  --green-dim:  rgba(16,185,129,0.10);

  /* Gradients */
  --grad-teal:   linear-gradient(135deg, #00d4b4, #0ea5e9);
  --grad-blue:   linear-gradient(135deg, #3b82f6, #6366f1);
  --grad-purple: linear-gradient(135deg, #a855f7, #ec4899);
  --grad-green:  linear-gradient(135deg, #10b981, #06b6d4);
  --grad-amber:  linear-gradient(135deg, #f59e0b, #f97316);
  --grad-rose:   linear-gradient(135deg, #f43f5e, #a855f7);

  /* Spacing */
  --r:    14px;
  --r-sm: 10px;
  --r-lg: 20px;
  --gap:  16px;

  /* Shadows */
  --shadow-sm: 0 4px 16px rgba(0,0,0,0.3);
  --shadow:    0 8px 32px rgba(0,0,0,0.45);
  --shadow-lg: 0 20px 60px rgba(0,0,0,0.6);
  --shadow-teal:   0 12px 40px rgba(0,212,180,0.18);
  --shadow-blue:   0 12px 40px rgba(59,130,246,0.18);
  --shadow-purple: 0 12px 40px rgba(168,85,247,0.18);
  --shadow-green:  0 12px 40px rgba(16,185,129,0.18);
  --shadow-amber:  0 12px 40px rgba(245,158,11,0.18);
}
```

### Background Mesh Effect:
```css
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background:
    radial-gradient(ellipse 80% 60% at 15% -5%,  rgba(0,212,180,0.07)  0%, transparent 60%),
    radial-gradient(ellipse 60% 50% at 85% 110%, rgba(168,85,247,0.08)  0%, transparent 60%),
    radial-gradient(ellipse 40% 40% at 50% 50%,  rgba(59,130,246,0.03)  0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
}
```

### Grid Noise Texture (subtle grain):
```css
body::after {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,..."); /* SVG noise pattern */
  opacity: 0.02;
  pointer-events: none;
  z-index: 0;
}
```

---

## ✨ ANIMATION SYSTEM

### Easing Functions:
```css
--ease-spring:  cubic-bezier(0.34, 1.56, 0.64, 1);  /* springy hover lifts */
--ease-out:     cubic-bezier(0.22, 1, 0.36, 1);       /* page entrances */
--ease-smooth:  cubic-bezier(0.4, 0, 0.2, 1);         /* data transitions */
```

### Page Load Sequence (orchestrated, staggered):

| Step | Element | Delay | Duration | Effect |
|------|---------|-------|----------|--------|
| 0 | Loader screen | 0ms | 800ms | Logo pulse + progress bar fills |
| 1 | Loader exit | 800ms | 400ms | Fade out + slide up |
| 2 | Header | 900ms | 500ms | Slide down from top |
| 3 | Filter bar | 1000ms | 400ms | Fade up |
| 4 | KPI card 1 | 1100ms | 400ms | Fade up + scale from 0.95 |
| 5 | KPI card 2 | 1150ms | 400ms | Same |
| 6 | KPI card 3 | 1200ms | 400ms | Same |
| 7 | KPI card 4 | 1250ms | 400ms | Same |
| 8 | KPI card 5 | 1300ms | 400ms | Same |
| 9 | Secondary stats | 1350ms | 400ms | Fade up |
| 10 | Chart cards | 1400ms+ | 500ms | Fade up, each +80ms stagger |
| 11 | Insights | 1800ms | 400ms | Slide up |
| 12 | Footer | 1900ms | 300ms | Fade in |

### KPI Counter Animation:
```js
function animateCounter(el, target, prefix = '', suffix = '', decimals = 0) {
  const duration = 1000;
  const startTime = performance.now();
  function step(now) {
    const t = Math.min((now - startTime) / duration, 1);
    const ease = 1 - Math.pow(1 - t, 3); // cubic ease-out
    const value = target * ease;
    el.textContent = prefix + value.toLocaleString('en-US', {
      minimumFractionDigits: decimals,
      maximumFractionDigits: decimals
    }) + suffix;
    if (t < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}
```

### Micro-Interactions Checklist:
- ✅ Filter dropdown: chevron rotates 180° when open
- ✅ Filter dropdown: teal focus ring glow on focus
- ✅ Reset button: icon spins 360° on click
- ✅ KPI cards: number flashes teal briefly on update
- ✅ Chart tooltips: custom dark glass style (no browser default)
- ✅ Chart hover: data point grows + glows
- ✅ Card hover: `translateY(-4px)` + colored shadow + top border reveal
- ✅ Insight cards: staggered slide-in on each filter change
- ✅ Filter chips: slide in with spring, slide out with fade on dismiss
- ✅ Heatmap cells: color transition on hover + tooltip
- ✅ Treemap blocks: scale + border glow on hover

---

## 🧩 COMPLETE DASHBOARD STRUCTURE

### SECTION 1 — HEADER (Sticky Glass Bar)

┌──────────────────────────────────────────────────────────────────────┐
│  [E]  Executive Sales Dashboard          [● Live]  [FY 2018–2021]   │
│       Real-time performance intelligence · 500 orders analyzed       │
└──────────────────────────────────────────────────────────────────────┘

**Specs:**
- Height: 64px
- `position: sticky; top: 0; z-index: 100`
- `backdrop-filter: blur(24px) saturate(180%)`
- `background: rgba(7,11,18,0.88)`
- `border-bottom: 1px solid var(--border)`
- Logo badge: 36×36px, `var(--grad-teal)`, rounded 10px, letter "E" in white bold mono
- "Live" badge: teal, pulsing dot `●` animation every 2s
- Version badge: muted border, subtle text

---

### SECTION 2 — FILTER BAR

**Layout:** `flex-wrap: wrap; gap: 10px; align-items: flex-end`

**5 Dropdowns:**
| Label | ID | Options |
|-------|----|---------|
| Year | f-year | All Years, 2018, 2019, 2020, 2021 |
| Region | f-region | All Regions, Central, East, South, West |
| Segment | f-segment | All Segments, Consumer, Corporate, Home Office |
| Category | f-category | All Categories, Furniture, Office Supplies, Technology |
| Ship Mode | f-shipmode | All Modes, First Class, Same Day, Second Class, Standard Class |

**Dropdown Styling:**
```css
select {
  background: #0d1220;          /* solid — options always visible */
  color: var(--text);
  border: 1px solid var(--border);
  border-radius: var(--r-sm);
  padding: 8px 32px 8px 12px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  min-width: 140px;
  appearance: none;
  cursor: pointer;
  transition: border-color 0.2s, box-shadow 0.2s;
}
select option {
  background: #0d1220;
  color: #e2e8f4;
}
select:focus {
  outline: none;
  border-color: rgba(0,212,180,0.5);
  box-shadow: 0 0 0 3px rgba(0,212,180,0.08);
}
```

**Active Filter Chips (below dropdowns):**
- Appears only when filters are active
- Each chip: `[Category: Technology ×]` — dismissible with × button
- Chips styled: teal border + teal-dim background + teal text
- Chip dismiss: calls `resetSingleFilter(key)` and re-runs charts

**Active Filter Count Badge:**
- Shows "3 active filters" next to reset button when > 0 filters set
- Disappears when all reset

**Reset Button:**

[↺ Reset Filters]

- On click: icon rotates 360°, all filters clear, chips remove, charts update

---

### SECTION 3 — KPI CARDS (5 cards)

**Grid:** `grid-template-columns: repeat(5, 1fr); gap: 14px`

| # | Title | Icon | Accent | Formula |
|---|-------|------|--------|---------|
| 1 | Total Revenue | 💰 | Teal | `sum(sales)` |
| 2 | Net Profit | 📈 | Green | `sum(profit)` |
| 3 | Profit Margin | 🎯 | Blue | `sum(profit)/sum(sales)*100` |
| 4 | Total Orders | 📦 | Purple | `count(records)` |
| 5 | Avg Order Value | 💳 | Amber | `sum(sales)/count(records)` |

**Each Card Structure:**
```html
<div class="kpi-card c-[color]">
  <div class="kpi-top">
    <div class="kpi-icon">[emoji]</div>
    <div class="kpi-sparkline"><canvas></canvas></div>  <!-- mini 8pt line -->
  </div>
  <div class="kpi-label">Total Revenue</div>
  <div class="kpi-value" id="kpi-revenue">$0</div>
  <div class="kpi-trend">
    <span class="trend-arrow">↑</span>
    <span class="trend-pct">12.4%</span>
    <span class="trend-label">vs prior period</span>
  </div>
</div>
```

**Sparkline:** 8-point mini line chart inside each KPI card
- Shows last 8 months of the metric
- No axes, no labels — just the shape
- Color matches card accent
- Height: ~36px, width: ~80px

**Trend Calculation:**
- Compare `filtered data for current year` vs `same filters for previous year`
- If no year filter set: compare 2021 vs 2020
- Show `↑ X%` in green or `↓ X%` in rose

**Card Hover Effects:**
```css
.kpi-card:hover {
  transform: translateY(-5px);
  border-color: var(--border-hi);
  background: rgba(255,255,255,0.06);
}
.kpi-card:hover::before { opacity: 1; } /* top border gradient line */
.kpi-card.c-teal:hover { box-shadow: var(--shadow-teal); }
```

---

### SECTION 4 — SECONDARY METRIC STRIP (3 cards, slim)

**Grid:** `grid-template-columns: repeat(3, 1fr); gap: 14px`

| Card | Value | Icon | Color |
|------|-------|------|-------|
| Return Rate | `(returned/total*100).toFixed(1)%` | 🔄 | Rose |
| Avg Customer Rating | Star display `★★★★☆` + number | ⭐ | Amber |
| Avg Discount | `(avg discount * 100).toFixed(1)%` | 🏷️ | Indigo |

**Star Rating Display:**
```js
function renderStars(rating) {
  const full = Math.round(rating);
  return '★'.repeat(full) + '☆'.repeat(5 - full);
}
```

---

### SECTION 5 — CHART GRID (10 charts total)

All charts use **Chart.js 4.x**.  
All charts: `responsive: true`, `maintainAspectRatio: false`, custom tooltip.  
Destroy and recreate on each filter change — never update in place.

#### Global Chart Tooltip Config:
```js
const tooltipDefaults = {
  backgroundColor: 'rgba(7,11,18,0.96)',
  borderColor: 'rgba(255,255,255,0.1)',
  borderWidth: 1,
  padding: 14,
  cornerRadius: 10,
  titleColor: '#e2e8f4',
  bodyColor: '#64748b',
  titleFont: { family: "'JetBrains Mono', monospace", weight: '700', size: 13 },
  bodyFont:  { family: "'Inter', sans-serif", size: 12 },
  displayColors: true,
  boxWidth: 10,
  boxHeight: 10,
  boxPadding: 4,
};
```

---

#### CHART A — Revenue & Profit Trend *(2/3 width, tall)*

**Type:** Line  
**X-axis:** Month labels (Jan 2018 … Dec 2021) or grouped by Quarter/Year  
**Y-axis:** Dollar values  
**Datasets:**
- Revenue: `--teal`, gradient fill top→transparent
- Profit: `--blue`, gradient fill top→transparent

**Toggle Buttons (above chart):**

[Monthly]  [Quarterly]  [Yearly]

- Active button: filled teal bg + white text
- Inactive: ghost border
- On click: re-aggregate data, re-render chart

**Features:**
- `tension: 0.4` smooth curves
- `pointRadius: 0`, `pointHoverRadius: 6`
- Crosshair plugin (draw vertical line on hover)
- Dual legend (Revenue + Profit) shown above chart

---

#### CHART B — Category Share *(1/3 width, tall)*

**Type:** Doughnut  
**Cutout:** 68%  
**Segments:** Furniture, Office Supplies, Technology  
**Colors:** `--blue`, `--teal`, `--purple`  
**Center Label:** Total revenue value (drawn via plugin)  
**Legend:** Below chart with colored dots + name + %  
**Hover:** Segment expands `hoverOffset: 12`

---

#### CHART C — Regional Performance *(1/3 width)*

**Type:** Bar (grouped)  
**Groups:** East, West, Central, South (sorted by revenue desc)  
**Datasets:**
- Revenue bars: `--teal` at 60% opacity
- Profit bars: `--blue` at 60% opacity
**Border radius:** 6px  
**Legend:** shown  
**Y-axis callback:** `'$' + value.toLocaleString()`

---

#### CHART D — Segment Growth *(1/3 width)*

**Type:** Bar (stacked)  
**X-axis:** Years 2018–2021  
**Stack groups:** Consumer (`--teal`), Corporate (`--blue`), Home Office (`--purple`)  
**Border radius:** 4px  
**Both axes stacked:** true  
**Legend:** shown

---

#### CHART E — Ship Mode Volume *(1/3 width)*

**Type:** Horizontal Bar  
**Y-axis:** Ship modes sorted by volume desc  
**X-axis:** Order count  
**Bar fill:** gradient from `--indigo` to `--cyan`  
**Percentage label:** drawn at end of each bar using `afterDatasetsDraw` plugin  
**Border radius:** 6px

---

#### CHART F — Top 10 States *(1/2 width)*

**Type:** Horizontal Bar  
**Y-axis:** Top 10 states by revenue (sorted desc)  
**X-axis:** Revenue in $  
**Fill:** gradient `--teal` → `--blue`  
**Value labels:** inside bar end  
**Border radius:** 5px

---

#### CHART G — Sales vs Profit Scatter *(1/2 width)*

**Type:** Bubble  
**X-axis:** Sales ($)  
**Y-axis:** Profit ($)  
**Bubble radius:** `quantity * 1.5`  
**Color by category:**
- Furniture: `--blue`
- Office Supplies: `--teal`
- Technology: `--purple`

**Quadrant Lines:**
- Draw average sales (vertical dashed line) and average profit (horizontal dashed line)
- Use `afterDraw` plugin
- Label quadrants: "High Value", "High Vol / Low Margin", etc.

**Legend:** shown

---

#### CHART H — Discount Impact Analysis *(full width)*

**Type:** Line  
**X-axis:** Discount buckets: 0%, 5%, 10%, 15%, 20%  
**Datasets:**
- Avg Profit per bucket: `--amber` line + amber fill
- Avg Sales per bucket: `--teal` line + teal fill

**Annotations (drawn with afterDraw plugin):**
- Vertical dashed line at 15% labeled "⚠ Risk Zone"
- Horizontal dashed line at overall avg profit labeled "Avg Profit"

**Features:**
- `tension: 0.4` smooth curves
- `pointRadius: 5`, `pointHoverRadius: 8`
- Both lines shown in legend

---

#### CHART I — Monthly Revenue Heatmap *(1/2 width, pure JS/CSS)*

**No Chart.js — build with CSS Grid:**

2018    2019    2020    2021
Jan      [cell] [cell] [cell] [cell]
Feb      [cell] [cell] [cell] [cell]
...
Dec      [cell] [cell] [cell] [cell]

**Cell Specs:**
- Size: flexible (fill container)
- Color intensity: map revenue to `rgba(0, 212, 180, opacity)` where `opacity = value/max`
- Minimum opacity: 0.05 (never fully invisible)
- Border: 2px solid var(--bg) (gap between cells)
- Border radius: 4px
- Hover: `outline: 2px solid var(--teal)` + custom tooltip div

**Tooltip on hover:**

Jan 2020
Revenue: $24,832

- Positioned absolutely near cursor
- Dark glass style matching chart tooltips

**Legend strip below grid:**

Low ░░▒▒▓▓██ High

---

#### CHART J — Sub-Category Revenue Treemap *(1/2 width, pure JS/CSS)*

**No Chart.js — build with nested CSS flex/grid:**

**Structure:**
- Outer blocks: one per Category (Furniture / Office Supplies / Technology)
- Inner blocks: one per Sub-Category, width proportional to revenue share
- Category label: top-left inside outer block
- Sub-category label: centered inside inner block (hide if too small)

**Colors:**
- Furniture outer: `--blue-dim` border + `--blue` label
- Office Supplies outer: `--teal-dim` border + `--teal` label
- Technology outer: `--purple-dim` border + `--purple` label
- Inner blocks: lighter shade of parent color

**Hover effect on inner block:**
- `transform: scale(1.03)` + glow border + tooltip with exact revenue + % share

**Algorithm (squarified treemap approximation):**
```js
// Sort sub-categories by revenue desc
// Assign flex-grow proportional to revenue
// Use nested flex rows inside category containers
```

---

### SECTION 6 — INSIGHTS PANEL

**Title:**

✦ AI-Powered Insights  ──────────────────────────────────

- Section title with decorative line extending to edge
- Updates label: `"Updated just now"` in muted text (right-aligned)

**Layout:** `grid-template-columns: repeat(5, 1fr); gap: 12px`  
On mobile: `repeat(2, 1fr)` then `1fr`

**6 Insight Cards (show 5, pick best):**

| # | Icon | Trigger | Headline Formula | Stat Line |
|---|------|---------|-----------------|-----------|
| 1 | 📈 | Always | "[TopCategory] leads profit" | "$X profit · Y% margin" |
| 2 | ⚠️ | discount avg > 10% | "Discount pressure detected" | "X orders avg $Y profit at 15%+ discount" |
| 3 | 🌍 | Always | "[TopRegion] dominates revenue" | "$X · Y% of total" |
| 4 | ✅/🔶/🔴 | Always | "Margin health: [status]" | "X% overall · target is 15%" |
| 5 | 📦 | Always | "Q4 seasonal peak confirmed" | "Q4 averages X% more than Q1" |
| 6 | 🚀 | yoy growth > 10% | "Strong YoY growth" | "2021 up X% vs 2020" |

**Card Anatomy:**
```html
<div class="insight-card">
  <div class="insight-icon-wrap">[emoji]</div>
  <div class="insight-headline">Technology leads profit</div>
  <div class="insight-stat">$184,230 profit · 28% margin</div>
  <div class="insight-bar">
    <div class="insight-bar-fill" style="width: 74%; background: var(--grad-teal)"></div>
  </div>
</div>
```

**Progress Bar:** relative value bar at bottom of each insight card  
- Width = normalized metric value (e.g., margin/50 capped at 100%)
- Adds visual weight to each insight

**Animation on filter change:**
- Cards fade out (150ms)
- Data recalculates
- Cards stagger back in (each +60ms delay, spring easing)

---

### SECTION 7 — FOOTER

Executive Sales Dashboard  ·  Powered by Chart.js  ·  FY 2018–2021  ·  500 orders analyzed  ·  © 2026

- `padding: 32px`
- `text-align: center`
- `color: var(--text-dim)`
- `font-size: 11px`
- `letter-spacing: 0.5px`
- `border-top: 1px solid var(--border)`

---

## 📐 RESPONSIVE BREAKPOINTS

| Screen | KPI Grid | Chart Grid | Insights |
|--------|----------|------------|----------|
| > 1400px | 5 cols | 3 cols | 5 cols |
| 1200–1400px | 3 cols | 2 cols | 3 cols |
| 900–1200px | 2 cols | 2 cols | 2 cols |
| 600–900px | 2 cols | 1 col | 2 cols |
| < 600px | 1 col | 1 col | 1 col |

**On mobile:**
- Header: hide subtitle, compress logo
- Filters: horizontal scroll row
- KPI values: slightly smaller font
- Charts: full width, height reduced to 200px
- Heatmap: horizontally scrollable

---

## ⚙️ JAVASCRIPT ARCHITECTURE

Structure all JS in clearly separated sections with comments:

```js
// ════════════════════════════════════════
// 1. CONFIG
// ════════════════════════════════════════
// Color maps, margin configs, constants

// ════════════════════════════════════════
// 2. DATA GENERATION
// ════════════════════════════════════════
// generateData() — 500 records, all rules applied

// ════════════════════════════════════════
// 3. FILTER ENGINE
// ════════════════════════════════════════
// applyFilters()
// resetFilters()
// resetSingleFilter(key)
// updateFilterChips()
// updateActiveFilterBadge()

// ════════════════════════════════════════
// 4. KPI ENGINE
// ════════════════════════════════════════
// updateKPIs()
// animateCounter(el, target, prefix, suffix, decimals)
// buildSparkline(canvasEl, data, color)
// computeTrend(currentData, allData, metric)

// ════════════════════════════════════════
// 5. SECONDARY STATS
// ════════════════════════════════════════
// updateSecondaryStats()
// renderStars(rating)

// ════════════════════════════════════════
// 6. CHARTS (one function each)
// ════════════════════════════════════════
// buildTrendChart(viewMode)   // monthly|quarterly|yearly
// buildDonutChart()
// buildRegionChart()
// buildSegmentChart()
// buildShipModeChart()
// buildStatesChart()
// buildBubbleChart()
// buildDiscountChart()

// ════════════════════════════════════════
// 7. HEATMAP (pure JS/CSS)
// ════════════════════════════════════════
// buildHeatmap()
// showHeatmapTooltip(evt, month, year, value)

// ════════════════════════════════════════
// 8. TREEMAP (pure JS/CSS)
// ════════════════════════════════════════
// buildTreemap()
// computeTreemapLayout(data)

// ════════════════════════════════════════
// 9. INSIGHTS ENGINE
// ════════════════════════════════════════
// computeInsights()
// renderInsights(insights)
// getMarginStatus(margin)

// ════════════════════════════════════════
// 10. CHART REGISTRY (destroy/rebuild)
// ════════════════════════════════════════
// const chartRegistry = {}
// function destroyChart(id)
// function registerChart(id, instance)

// ════════════════════════════════════════
// 11. INIT & ORCHESTRATION
// ════════════════════════════════════════
// initFilters()
// runAll()           // called on filter change
// pageLoadSequence() // staggered animations on DOMContentLoaded
```

### Chart Registry Pattern (prevent canvas memory leak):
```js
const chartRegistry = {};

function destroyChart(id) {
  if (chartRegistry[id]) {
    chartRegistry[id].destroy();
    delete chartRegistry[id];
  }
}

function registerChart(id, chartInstance) {
  destroyChart(id);
  chartRegistry[id] = chartInstance;
  return chartInstance;
}
```

### Trend View Toggle (Chart A):
```js
let trendView = 'monthly'; // 'monthly' | 'quarterly' | 'yearly'

function aggregateTrendData(data, view) {
  // monthly: group by "YYYY-MM"
  // quarterly: group by "YYYY-Q1"
  // yearly: group by "YYYY"
  // return { labels[], salesData[], profitData[] }
}
```

---

## 🔌 EXTERNAL DEPENDENCIES (CDN only)

```html
<!-- Chart.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>

<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
```

**Nothing else. No D3. No Lodash. No jQuery. No additional Chart.js plugins.**  
All heatmap, treemap, annotations, crosshair drawn with vanilla JS canvas or CSS.

---

## 🧪 FINAL QUALITY CHECKLIST

Work through every item before outputting. Do not output until all are checked.

### ✅ Data Integrity
- [ ] Exactly 500 records generated
- [ ] Zero records with negative profit
- [ ] Q4 revenue visibly higher than Q1 in trend chart
- [ ] 2021 revenue visibly higher than 2018 (YoY growth)
- [ ] Cities match their states
- [ ] Discount never exceeds 20%
- [ ] Rating logic follows discount/profit rules

### ✅ UI & Layout
- [ ] Loader screen appears and transitions out cleanly
- [ ] Header is sticky and glass effect works
- [ ] All 5 KPIs animate on load and on filter change
- [ ] Sparklines render inside KPI cards
- [ ] Secondary stats row renders correctly
- [ ] Star rating renders correctly
- [ ] Filter chips appear when filters active
- [ ] Active filter count badge shows correctly
- [ ] Reset button spins icon on click
- [ ] All filter options are visible (solid dark bg on select/option)
- [ ] Footer present

### ✅ Charts
- [ ] Chart A (Trend) renders with toggle buttons working
- [ ] Chart B (Donut) renders with center label
- [ ] Chart C (Region bar) renders grouped
- [ ] Chart D (Segment stacked) renders correctly
- [ ] Chart E (Ship mode horizontal) renders with % labels
- [ ] Chart F (Top states horizontal) renders top 10
- [ ] Chart G (Bubble/scatter) renders with quadrant lines
- [ ] Chart H (Discount line) renders with annotations
- [ ] Chart I (Heatmap) renders as CSS grid with hover tooltip
- [ ] Chart J (Treemap) renders with proportional blocks
- [ ] All chart tooltips are custom styled
- [ ] No canvas errors or Chart.js warnings in console
- [ ] All charts destroyed and recreated on filter change

### ✅ Insights
- [ ] 5 insight cards render
- [ ] All values computed from filtered data
- [ ] Cards animate out and in on filter change
- [ ] Progress bars render inside each card
- [ ] Icons display correctly

### ✅ Interactions
- [ ] All 5 filters work and cascade across all charts
- [ ] Single filter reset (chip dismiss) works
- [ ] Full reset works
- [ ] Trend view toggle (Monthly/Quarterly/Yearly) works
- [ ] Heatmap hover tooltip appears and follows cursor
- [ ] Treemap block hover scales and shows tooltip
- [ ] KPI card hover lift and glow works
- [ ] Chart card hover lift works

### ✅ Responsiveness
- [ ] Layout adapts at 1200px, 900px, 600px, 375px
- [ ] No horizontal overflow on mobile
- [ ] Filters are scrollable on mobile
- [ ] Charts resize correctly on window resize

### ✅ Performance & Code
- [ ] No console errors
- [ ] No memory leaks (chart registry pattern used)
- [ ] Animations run at 60fps
- [ ] Code is organized in sections with comments
- [ ] No inline event handlers — use `addEventListener`

---

## 🚨 ABSOLUTE OUTPUT RULES

1. Output **ONE complete self-contained `.html` file**
2. **No explanation text** before or after the HTML
3. **No markdown code fences** wrapping the output
4. **No placeholder comments** like `// add chart here` — all code must be complete
5. **No TODO items** — everything must be implemented
6. If any chart or feature is not implemented, the output is **incomplete and must be redone**
7. Test mentally: open the file in a browser → everything works, no errors, looks premium

---

## 💎 PREMIUM BAR

The final output must feel indistinguishable from a **real enterprise SaaS dashboard**.

Ask yourself before outputting:
- Does it look better than a generic Chart.js tutorial?
- Would a Fortune 500 company use this for an executive meeting?
- Are the animations smooth and purposeful, not gimmicky?
- Is every pixel intentional?
- Does the color system feel cohesive?
- Does it feel **alive** — responding to interactions with delight?

**If the answer to any of these is NO — improve it before outputting.**
