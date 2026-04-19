# ScootyPro — Complete E-Commerce Website Prompt

## TASK
Build a 100% complete, production-ready, single HTML file e-commerce website for a Pakistani scooter dealership called **ScootyPro**. Everything must be in ONE file: HTML + CSS + JavaScript. No external files except CDN links.

---

## TECH STACK
- **TailwindCSS**: `https://cdn.tailwindcss.com`
- **Font Awesome 6**: `https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css`
- **Google Fonts**: Rajdhani (headings) + Inter (body)
- **No frameworks, no Vue, no React** — pure Vanilla JS only

---

## BRAND
- Name: **ScootyPro**
- Tagline: **"Ride in Style, Ride with Power"**
- WhatsApp: `+923022311916`
- Primary Color: `#1D4ED8` (deep blue)
- Yellow: `#EAB308`
- Red: `#DC2626`
- Dark BG: `#0F172A`
- Light BG: `#F8FAFC`

---

## IMAGE FILES (local — all in same folder as index.html)
- `logo.png` — brand logo
- `hero.png` — hero background (opacity 35%, used as texture)
- `premium.png` — about section image (object-fit: cover, height 460px)
- `product1.png` to `product10.png` — scooter images (**object-fit: CONTAIN**, NOT cover)
- `gallery1.png` to `gallery4.png` — gallery images (**object-fit: CONTAIN**, NOT cover)

**CRITICAL**: Product and gallery images MUST use `object-fit: contain` with padding so scooters are never cropped. Background of image containers should be a light gradient (e.g. `linear-gradient(145deg, #eef2ff, #ffffff, #f0f9ff)`).

---

## PRODUCTS DATA (JavaScript array)

```js
const products = [
  { id:1,  name:'Breeze 100',  price:85000,  cat:'commute', img:'product1.png',  engine:'100cc', mileage:'45km/L', speed:'65km/h',
  desc:'100cc 4-stroke engine, ideal for daily city commute. Smooth ride, great fuel efficiency.' },
  { id:2,  name:'Sport 125',   price:105000, cat:'sport',   img:'product2.png',  engine:'125cc', mileage:'38km/L', speed:'90km/h',
  desc:'Sport-tuned 125cc engine with disc brake, alloy wheels and aggressive styling.' },
  { id:3,  name:'Classic 100', price:88000,  cat:'commute', img:'product3.png',  engine:'100cc', mileage:'48km/L', speed:'65km/h',
  desc:'Retro-inspired design with comfortable seat and ultra smooth ride quality.' },
  { id:4,  name:'Thunder 150', price:125000, cat:'sport',   img:'product4.png',  engine:'150cc', mileage:'35km/L', speed:'110km/h',
  desc:'150cc powerhouse with digital speedometer, LED headlights and premium build.' },
  { id:5,  name:'Petal 100',   price:80000,  cat:'ladies',  img:'product5.png',  engine:'100cc', mileage:'45km/L', speed:'65km/h',
  desc:'Stylish ladies scooter — step-through frame, only 95kg, easy to handle.' },
  { id:6,  name:'Urban 125',   price:95000,  cat:'commute', img:'product6.png',  engine:'125cc', mileage:'40km/L', speed:'85km/h',
  desc:'City commuter with 18L under-seat storage, USB charging port and smart design.' },
  { id:7,  name:'Eco 100',     price:82000,  cat:'commute', img:'product7.png',  engine:'100cc', mileage:'55km/L', speed:'65km/h',
  desc:'Ultra fuel-efficient at 55km/L. Low emission, best choice for eco-conscious riders.' },
  { id:8,  name:'Turbo 150',   price:130000, cat:'sport',   img:'product8.png',  engine:'150cc', mileage:'32km/L', speed:'115km/h',
  desc:'Top-of-the-line 150cc performance scooter. Racing DNA, sport exhaust, 0–60 in 6.5s.' },
  { id:9,  name:'Blossom 110', price:86000,  cat:'ladies',  img:'product9.png',  engine:'110cc', mileage:'44km/L', speed:'70km/h',
  desc:'Elegant ladies model with pastel colors, automatic choke and easy self-start.' },
  { id:10, name:'Swift 100',   price:83000,  cat:'commute', img:'product10.png', engine:'100cc', mileage:'50km/L', speed:'65km/h',
  desc:'Lightweight at only 90kg. Nimble handling, perfect for narrow city streets.' },
];
```

---

## ALL SECTIONS (16 total — in exact order)

### 1. STICKY HEADER

- logo.png left (height 48px, object-fit:contain)
- "ScootyPro" text in blue next to logo
- Desktop nav: Home, Products, About, Gallery, Contact (smooth scroll anchors)
- Right: cart icon button with red badge + "Book Now" blue pill button
- Mobile: hamburger opens dropdown nav
- On scroll > 50px: add box-shadow to header
- Nav links: underline animation on hover (CSS ::after width 0→100%)

### 2. HERO SECTION (full viewport height)

- Background: dark navy #0a0f1e with hero.png at 35% opacity as texture
- Subtle dot-grid pattern overlay: radial-gradient(rgba(29,78,216,0.08) 1px, transparent 1px)
- Blue glow blob top-right, yellow glow blob bottom-left
- Two-column layout (desktop): left text, right featured product card
- Left side:
  - Animated badge pill: "🏍️ Pakistan's #1 Scooter Destination"
  - H1: "Ride in Style," (white) + "Ride with Power" (yellow #EAB308)
  - Subtitle paragraph (white 65% opacity)
  - 4 feature pills: Free Delivery (green icon) | 1-Year Warranty (blue) | Easy Installments (yellow) | COD Available (red)
  - Two CTA buttons: "Explore Scooters" (blue solid, border-radius 14px) + "WhatsApp Order" (green #25D366)
  - Buttons lift on hover (translateY -3px)
- Right side (dark glass card):
  - Shows product1.png in a dark container (object-fit:contain, padding 20px)
  - "⚡ Featured" yellow badge on image
  - Below: product name, engine/mileage/speed mini-stat cards
  - "Quick View" button (calls openQuickView(1))
  - Scroll indicator below card (two vertical lines + "SCROLL DOWN" text)
- Bottom stats bar (dark semi-transparent, border-top):
  - 4 stats in grid: 10,000+ Happy Riders | 1 Year Warranty | Free Delivery | 5.0 ★ Rating
  - With subtle right-border dividers between stats
- Mobile: stack to single column, text centered

### 3. TRUST MARQUEE BAR

- Dark blue #1D4ED8 background
- Infinite scrolling marquee (CSS animation, 30s)
- 8 items × 2 (duplicate for seamless loop):
  Free Delivery | 1-Year Warranty | Easy Installments | 24/7 Support |
  Free 1st Service | 5-Star Rated | Same-Day Dispatch | Pan-Pakistan
- Each item: Font Awesome icon (yellow #EAB308) + white text
- Pause on hover

### 4. PRODUCTS SECTION

- Section heading + subheading, fade-up on scroll
- Category filter pills: All Scooters | 🏙️ Commute | ⚡ Sport | 🌸 Ladies
  - Active: solid #1D4ED8 bg, white text, box-shadow
  - Inactive: white bg, blue border, blue text, hover: light blue bg
- Product grid: grid-template-columns: repeat(3, 1fr) desktop, 2 tablet, 1 mobile
- Products rendered via JavaScript renderProducts() function

**Product Card design (very important):**

```
┌─────────────────────────────┐
│ [Category badge top-left]   │
│                             │
│   Image (contain, 230px,    │
│   gradient bg, no crop)     │
│                             │
│ [Quick View slides up on    │
│  hover from bottom]         │
├─────────────────────────────┤
│ ★★★★★ (4.9)                │
│ Product Name (Rajdhani bold)│
│ Short description (2 lines) │
│ [Engine][Mileage][Speed]    │
│ PKR X,XX,XXX /unit          │
│ [Add Cart] [Buy Now]        │
└─────────────────────────────┘
```

- Card hover: translateY(-10px) + box-shadow: 0 32px 64px rgba(29,78,216,0.22)
- Image hover: scale(1.1) (smooth 0.55s cubic-bezier)
- "Quick View" button: slides up from bottom on card hover (CSS: bottom -50px → 12px)
- Category badge colors: commute=blue, sport=red, ladies=pink
- Each category gets matching subtle bg gradient in image area
- "Add to Cart": outline blue button (border 2px solid #1D4ED8, transparent bg)
- "Buy Now": solid blue gradient button with shadow

### 5. COUNTDOWN OFFER SECTION

- Dark gradient bg: linear-gradient(135deg, #0F172A, #1e2d5e)
- "🔥 Limited Time Festival Offer" red pill badge
- Heading: "Flat 15% OFF on Sport Series!"
- Live countdown timer: target date 3 days from now
- 4 yellow boxes (Days / Hours / Mins / Secs) with label below
- "Shop Now" yellow button

### 6. WHY CHOOSE US

- Light bg #F8FAFC
- 3 white cards in a row with hover lift:
  - 🏆 10,000+ Happy Riders
  - 🔧 Free First Service (1,000km included)
  - 💳 3–12 Easy Installments
- Each card: blue icon in blue circle, big stat, title, description

### 7. ABOUT SECTION

- White bg, 2-column grid
- Left: badge, heading "Pakistan's Most Trusted Scooter Dealer", paragraph, 4 checklist items (blue check icon), "Learn More" outline button
- Right: premium.png image (height 460px, object-fit: COVER, border-radius 1.75rem, overflow hidden)
  - Floating badge bottom-left: white card with trophy icon + "10,000+ Happy Riders"
  - Floating badge top-right: blue card "1 Year / Warranty"

### 8. SPECS SECTION

- Light bg, 4 cards in a row: 55 km/L | 110 km/h | 150cc | 1-Year
- Animated counter: numbers count up from 0 when scrolled into view
- IntersectionObserver triggers once

### 9. GALLERY SECTION

- Dark bg: linear-gradient(180deg, #0a0f1e, #0F172A, #0a0f1e)
- Subtle dot-grid pattern overlay
- 2×2 grid, each card same height (320px desktop, 260px mobile)
- gallery1.png to gallery4.png — object-fit: CONTAIN (NOT cover!)
- Image background: dark #1a2035
- Padding 16px inside each card so bike is fully visible
- Hover: scale(1.06) image + blue gradient overlay from bottom
- Overlay shows glass-morphism "View Full" button
- Bottom: WhatsApp "Request More Photos" link

### 10. INSTALLMENT PLANS

- 3 cards: Starter (20% down, 12mo) | Popular (30% down, 6mo) | Premium (40% down, 3mo)
- Middle "Popular" card: solid blue bg, white text, scale(1.04), "MOST POPULAR" badge
- Each card has feature list + "Apply via WhatsApp" button

### 11. REVIEWS

- 3 testimonial cards, white bg section
- Each: avatar circle (initial letter, blue gradient bg), name, city, 5 stars, review, "Verified Buyer" green badge
- Cards hover lift
- Reviews: Ahmed Raza (Lahore) | Fatima Khan (Karachi) | Hassan Ali (Islamabad)

### 12. INSTAGRAM/SOCIAL GRID

- 6-cell 3×2 grid using gallery1–4.jpg repeated
- Each: square, hover shows blue overlay + Instagram icon + "View Post"
- "Follow @ScootyPro_PK" CTA button

### 13. FAQ ACCORDION

- 6 questions, one open at a time
- Smooth max-height transition (0 → scrollHeight px)
- Chevron rotates 180° when open
- Border highlight when open (blue border)
- Questions:
  - a. What scooter brands do you carry?
  - b. Do you deliver across all of Pakistan?
  - c. Are installment plans available?
  - d. What does the warranty cover?
  - e. How long does delivery take?
  - f. Can I test ride before purchasing?

### 14. FINAL CTA

- Dark #0F172A bg
- "Ready to Hit the Road?" (white, huge)
- Two buttons: "Shop Scooters" (yellow #EAB308, dark text) + "WhatsApp Order" (green)

### 15. FOOTER

- Dark #0F172A bg
- Top: Logo + tagline + social icons (Facebook, Instagram, YouTube, TikTok)
- 4-column grid: Brand desc | Quick Links | Products | Contact
- Contact: Lahore address, +923022311916, info@scootypro.pk
- Bottom bar: © 2025 ScootyPro | Made in Pakistan 🇵🇰

---

## COMPLETE CSS ANIMATIONS (embed in <style> tag)

```css
@keyframes fadeInUp    { from{opacity:0;transform:translateY(35px)} to{opacity:1;transform:translateY(0)} }
@keyframes fadeInLeft  { from{opacity:0;transform:translateX(-30px)} to{opacity:1;transform:translateX(0)} }
@keyframes marquee     { from{transform:translateX(0)} to{transform:translateX(-50%)} }
@keyframes bounceSlow  { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-12px)} }
@keyframes scaleIn     { from{opacity:0;transform:scale(0.92)} to{opacity:1;transform:scale(1)} }
@keyframes toastSlide  { from{opacity:0;transform:translateY(24px)} to{opacity:1;transform:translateY(0)} }
@keyframes float       { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }

/* Hero staggered animations */
.hero-a1 { animation: fadeInUp 1s cubic-bezier(0.16,1,0.3,1) 0.1s both; }
.hero-a2 { animation: fadeInUp 1s cubic-bezier(0.16,1,0.3,1) 0.25s both; }
.hero-a3 { animation: fadeInUp 1s cubic-bezier(0.16,1,0.3,1) 0.4s both; }
.hero-a4 { animation: fadeInUp 1s cubic-bezier(0.16,1,0.3,1) 0.55s both; }
.hero-a5 { animation: fadeInUp 1s cubic-bezier(0.16,1,0.3,1) 0.7s both; }

/* Scroll reveal */
.fade-up { opacity:0; transform:translateY(40px); transition:opacity 0.75s ease, transform 0.75s ease; }
.fade-up.visible { opacity:1; transform:translateY(0); }

/* PRODUCT IMAGE — CRITICAL */
.product-img-wrap {
  position:relative; height:230px; overflow:hidden;
  background:linear-gradient(145deg,#eef2ff 0%,#ffffff 50%,#f0f9ff 100%);
}
.product-img {
  width:100%; height:100%;
  object-fit:contain;        /* CONTAIN — never crop scooters */
  object-position:center;
  padding:14px;
  transition:transform 0.55s cubic-bezier(0.25,0.46,0.45,0.94);
}
.product-card:hover .product-img { transform:scale(1.1); }

/* Quick View slide-up button */
.quick-view-btn {
  position:absolute; bottom:-50px; left:50%; transform:translateX(-50%);
  background:rgba(15,23,42,0.9); color:#fff; padding:8px 20px;
  border-radius:50px; font-size:0.8rem; font-weight:600;
  transition:bottom 0.35s ease; cursor:pointer; border:none; white-space:nowrap;
}
.product-card:hover .quick-view-btn { bottom:12px; }

/* GALLERY IMAGE — CONTAIN */
.gallery-item { overflow:hidden; border-radius:1.25rem; position:relative; cursor:pointer; background:#1a2035; }
.gallery-item img {
  width:100%; height:100%;
  object-fit:contain;        /* CONTAIN — full bike visible */
  padding:16px;
  transition:transform 0.6s cubic-bezier(0.25,0.46,0.45,0.94);
}
.gallery-item:hover img { transform:scale(1.06); }
.gallery-overlay {
  position:absolute; inset:0;
  background:linear-gradient(to top, rgba(29,78,216,0.85) 0%, rgba(15,23,42,0.2) 100%);
  display:flex; flex-direction:column; align-items:center; justify-content:flex-end;
  padding-bottom:1.5rem; opacity:0; transition:opacity 0.4s ease;
}
.gallery-item:hover .gallery-overlay { opacity:1; }

/* PRODUCT CARD */
.product-card {
  background:#fff; border-radius:1.25rem; overflow:hidden;
  box-shadow:0 2px 12px rgba(0,0,0,0.06); border:1px solid rgba(0,0,0,0.05);
  transition:transform 0.35s cubic-bezier(0.25,0.46,0.45,0.94), box-shadow 0.35s ease;
  cursor:pointer; display:flex; flex-direction:column;
}
.product-card:hover {
  transform:translateY(-10px);
  box-shadow:0 32px 64px rgba(29,78,216,0.22);
  border-color:rgba(29,78,216,0.15);
}

/* CART SIDEBAR */
.cart-sidebar {
  position:fixed; top:0; right:0; height:100%; width:440px; max-width:96vw;
  background:#fff; z-index:500; transform:translateX(110%);
  transition:transform 0.4s cubic-bezier(0.25,0.46,0.45,0.94);
  box-shadow:-12px 0 50px rgba(0,0,0,0.15); display:flex; flex-direction:column;
}
.cart-sidebar.open { transform:translateX(0); }
.cart-overlay {
  position:fixed; inset:0; background:rgba(15,23,42,0.6); z-index:499;
  opacity:0; pointer-events:none; transition:opacity 0.4s ease; backdrop-filter:blur(2px);
}
.cart-overlay.open { opacity:1; pointer-events:all; }

/* MODALS */
.modal-overlay {
  position:fixed; inset:0; background:rgba(15,23,42,0.75); z-index:600;
  display:flex; align-items:center; justify-content:center; padding:1rem;
  opacity:0; pointer-events:none; transition:opacity 0.3s ease; backdrop-filter:blur(4px);
}
.modal-overlay.open { opacity:1; pointer-events:all; }
.modal-box {
  background:#fff; border-radius:1.5rem; max-width:920px; width:100%;
  max-height:92vh; overflow-y:auto; animation:scaleIn 0.3s ease both;
}

/* FAQ */
.faq-body { max-height:0; overflow:hidden; transition:max-height 0.45s ease; }
.faq-item.open .faq-body { max-height:200px; }
.faq-chevron { transition:transform 0.35s ease; display:inline-block; }
.faq-item.open .faq-chevron { transform:rotate(180deg); }

/* TOAST */
.toast {
  position:fixed; bottom:2rem; right:2rem; background:#0F172A; color:#fff;
  padding:1rem 1.5rem; border-radius:1rem; font-size:0.9rem; font-weight:600;
  z-index:9999; display:flex; align-items:center; gap:0.6rem;
  box-shadow:0 12px 40px rgba(0,0,0,0.25); animation:toastSlide 0.4s ease both;
  border-left:4px solid #1D4ED8;
}

/* NAV LINK underline */
.nav-link { position:relative; color:#374151; font-weight:600; font-size:0.875rem; }
.nav-link::after {
  content:''; position:absolute; bottom:-4px; left:0;
  width:0; height:2px; background:#1D4ED8; border-radius:2px; transition:width 0.3s ease;
}
.nav-link:hover::after { width:100%; }
.nav-link:hover { color:#1D4ED8; }

/* FILTER PILLS */
.filter-pill {
  cursor:pointer; border-radius:9999px; padding:8px 22px;
  font-size:0.875rem; font-weight:700; border:2px solid #1D4ED8; transition:all 0.25s ease;
}
.filter-pill.active { background:#1D4ED8; color:#fff; box-shadow:0 6px 16px rgba(29,78,216,0.35); }
.filter-pill:not(.active) { background:#fff; color:#1D4ED8; }
.filter-pill:not(.active):hover { background:#eff6ff; }

/* QTY BUTTONS */
.qty-btn {
  width:34px; height:34px; display:inline-flex; align-items:center; justify-content:center;
  border:2px solid #1D4ED8; color:#1D4ED8; border-radius:8px;
  cursor:pointer; font-size:1rem; background:#fff; transition:all 0.2s;
}
.qty-btn:hover { background:#1D4ED8; color:#fff; }

/* MARQUEE */
.marquee-track { display:flex; width:max-content; animation:marquee 30s linear infinite; }
.marquee-track:hover { animation-play-state:paused; }

/* Responsive */
@media(max-width:900px) {
  .hero-inner { flex-direction:column !important; padding-top:5rem !important; }
}
@media(max-width:1023px) { #productsGrid { grid-template-columns:repeat(2,1fr) !important; } }
@media(max-width:639px)  { #productsGrid { grid-template-columns:1fr !important; } }
@media(max-width:640px)  {
  .gallery-grid { grid-template-columns:1fr !important; }
  .gallery-item { height:260px !important; }
}
```

---

## COMPLETE JAVASCRIPT FUNCTIONS

### Cart System

```js
let cart = JSON.parse(localStorage.getItem('sp_cart') || '[]');

function saveCart() { localStorage.setItem('sp_cart', JSON.stringify(cart)); }

function addToCart(id, qty = 1) {
  const p = products.find(x => x.id === id);
  if (!p) return;
  const ex = cart.find(x => x.id === id);
  if (ex) ex.qty += qty;
  else cart.push({ id, name:p.name, price:p.price, img:p.img, qty });
  saveCart();
  updateCartUI();
  showToast(p.name + ' added to cart! 🛵');
}

function removeFromCart(id) { cart = cart.filter(x => x.id !== id); saveCart(); updateCartUI(); renderCartItems(); }
function changeQty(id, delta) {
  const item = cart.find(x => x.id === id);
  if (item) { item.qty = Math.max(1, item.qty + delta); saveCart(); updateCartUI(); renderCartItems(); }
}
function cartTotal() { return cart.reduce((s, i) => s + i.price * i.qty, 0); }
function fmtPrice(n) { return n.toLocaleString(); }

function updateCartUI() {
  const total = cart.reduce((s, i) => s + i.qty, 0);
  const badge = document.getElementById('cartBadge');
  badge.textContent = total;
  badge.style.display = total > 0 ? 'flex' : 'none';
  document.getElementById('cartCountLabel').textContent = total + ' item' + (total !== 1 ? 's' : '');
}

function renderCartItems() {
  const container = document.getElementById('cartItemsContainer');
  const footer = document.getElementById('cartFooter');
  if (!cart.length) {
    container.innerHTML = '<div style="text-align:center;padding:3rem;color:#6b7280;"><i class="fas fa-shopping-cart" style="font-size:3rem;color:#e5e7eb;display:block;margin-bottom:1rem;"></i><p>Your cart is empty</p></div>';
    footer.style.display = 'none'; return;
  }
  container.innerHTML = cart.map(item => `
    <div style="display:flex;gap:12px;align-items:center;padding:12px 0;border-bottom:1px solid #f1f5f9;">
      <img src="${item.img}" style="width:70px;height:70px;object-fit:contain;background:#f8fafc;border-radius:12px;padding:6px;border:1px solid #e5e7eb;" />
      <div style="flex:1;min-width:0;">
        <p style="font-weight:700;color:#111827;font-size:0.9rem;">${item.name}</p>
        <p style="color:#1D4ED8;font-weight:700;font-size:0.875rem;">PKR ${fmtPrice(item.price)}</p>
        <div style="display:flex;align-items:center;gap:8px;margin-top:6px;">
          <button class="qty-btn" onclick="changeQty(${item.id},-1)"><i class="fas fa-minus" style="font-size:0.7rem;"></i></button>
          <span style="font-weight:700;min-width:24px;text-align:center;">${item.qty}</span>
          <button class="qty-btn" onclick="changeQty(${item.id},1)"><i class="fas fa-plus" style="font-size:0.7rem;"></i></button>
        </div>
      </div>
      <div style="display:flex;flex-direction:column;align-items:flex-end;gap:8px;">
        <p style="font-weight:800;color:#111827;">PKR ${fmtPrice(item.price * item.qty)}</p>
        <button onclick="removeFromCart(${item.id})" style="background:none;border:none;color:#DC2626;cursor:pointer;"><i class="fas fa-trash-alt"></i></button>
      </div>
    </div>
  `).join('');
  footer.style.display = 'block';
  footer.innerHTML = `
    <div style="display:flex;justify-content:space-between;margin-bottom:1rem;">
      <span>Total</span>
      <span style="font-weight:800;color:#1D4ED8;font-size:1.4rem;font-family:Rajdhani,sans-serif;">PKR ${fmtPrice(cartTotal())}</span>
    </div>
    <button onclick="openOrderModal()" style="width:100%;background:#1D4ED8;color:#fff;border:none;border-radius:12px;padding:14px;font-weight:700;font-size:1rem;cursor:pointer;"><i class="fas fa-credit-card"></i> Proceed to Checkout</button>
    <button onclick="cart=[];saveCart();updateCartUI();renderCartItems();" style="width:100%;margin-top:8px;background:none;border:1px solid #e5e7eb;border-radius:12px;padding:10px;font-weight:600;font-size:0.85rem;cursor:pointer;color:#6b7280;">
      <i class="fas fa-trash"></i> Clear Cart
    </button>
  `;
}

function openCart()  { document.getElementById('cartSidebar').classList.add('open'); document.getElementById('cartOverlay').classList.add('open'); renderCartItems(); }
function closeCart() { document.getElementById('cartSidebar').classList.remove('open'); document.getElementById('cartOverlay').classList.remove('open'); }
function buyNow(id)  { addToCart(id); openCart(); }
```

### Product Render & Filter

```js
function catBadge(cat) {
  const map = { commute:{label:'Commute',color:'background:#dbeafe;color:#1e40af;'},
    sport:{label:'Sport',color:'background:#fee2e2;color:#991b1b;'}, ladies:{label:'Ladies',color:'background:#fce7f3;color:#9d174d;'} };
  return map[cat] || { label:cat, color:'' };
}

function renderProducts(filter = 'all') {
  const grid = document.getElementById('productsGrid');
  const list = filter === 'all' ? products : products.filter(p => p.cat === filter);
  const catBg = { commute:'#eef2ff', sport:'#fff1f2', ladies:'#fdf4ff' };
  grid.innerHTML = list.map(p => {
    const badge = catBadge(p.cat);
    return `<div class="product-card fade-up" onclick="openQuickView(${p.id})">
      <div class="product-img-wrap" style="background:linear-gradient(145deg,${catBg[p.cat]||'#eef2ff'} 0%,#fff 55%,#f8faff 100%);">
        <img class="product-img" src="${p.img}" alt="${p.name}" onerror="this.parentElement.style.background='linear-gradient(135deg,#dbeafe,#eff6ff)'" />
        <button class="quick-view-btn" onclick="event.stopPropagation();openQuickView(${p.id})">
          <i class="fas fa-eye"></i> Quick View
        </button>
        <span style="position:absolute;top:12px;left:12px;font-size:0.68rem;font-weight:800;padding:4px 10px;border-radius:50px;text-transform:uppercase;${badge.color}">${badge.label}</span>
      </div>
      <div style="padding:1.1rem 1.25rem 1.25rem;display:flex;flex-direction:column;flex:1;">
        <div style="color:#EAB308;font-size:0.72rem;margin-bottom:6px;">★★★★★ <span style="color:#9ca3af;">(4.9)</span></div>
        <h3 style="font-weight:700;color:#111827;font-size:1.15rem;font-family:Rajdhani,sans-serif;margin-bottom:4px;">${p.name}</h3>
        <p style="color:#6b7280;font-size:0.8rem;line-height:1.55;margin-bottom:10px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;">${p.desc}</p>
        <div style="display:flex;gap:5px;flex-wrap:wrap;margin-bottom:10px;">
          <span style="font-size:0.7rem;font-weight:700;padding:3px 9px;border-radius:50px;background:#eef2ff;color:#3730a3;">${p.engine}</span>
          <span style="font-size:0.7rem;font-weight:700;padding:3px 9px;border-radius:50px;background:#f0fdf4;color:#166534;">${p.mileage}</span>
          <span style="font-size:0.7rem;font-weight:700;padding:3px 9px;border-radius:50px;background:#fff7ed;color:#9a3412;">${p.speed}</span>
        </div>
        <div style="color:#1D4ED8;font-weight:800;font-size:1.4rem;margin-bottom:12px;font-family:Rajdhani,sans-serif;">PKR ${fmtPrice(p.price)} <span style="font-size:0.75rem;color:#9ca3af;font-weight:500;">/unit</span></div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:auto;">
          <button onclick="event.stopPropagation();addToCart(${p.id})" style="border:2px solid #1D4ED8;color:#1D4ED8;background:transparent;border-radius:12px;padding:9px;font-size:0.8rem;font-weight:700;cursor:pointer;" onmouseover="this.style.background='#eff6ff'" onmouseout="this.style.background='transparent'">
            <i class="fas fa-cart-plus"></i> Add Cart
          </button>
          <button onclick="event.stopPropagation();buyNow(${p.id})" style="background:linear-gradient(135deg,#1D4ED8,#2563eb);color:#fff;border:none;border-radius:12px;padding:9px;font-size:0.8rem;font-weight:700;cursor:pointer;box-shadow:0 4px 12px rgba(29,78,216,0.3);" onmouseover="this.style.background='#1e40af'" onmouseout="this.style.background='linear-gradient(135deg,#1D4ED8,#2563eb)'">
            Buy Now <i class="fas fa-arrow-right" style="font-size:0.75rem;"></i>
          </button>
        </div>
      </div>
    </div>`;
  }).join('');
  observeFadeUp();
}

function filterProducts(cat, btn) {
  document.querySelectorAll('.filter-pill').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderProducts(cat);
}
```

### Quick View Modal

```js
let qvQty = 1;
let currentProduct = null;

function openQuickView(id) {
  const p = products.find(x => x.id === id);
  if (!p) return;
  currentProduct = p; qvQty = 1;
  const badge = catBadge(p.cat);
  let thumbs = '';
  for (let t = 0; t < 5; t++) {
    thumbs += `<div style="border-radius:8px;overflow:hidden;aspect-ratio:1;background:#fff;cursor:pointer;border:2px solid ${t===0?'#1D4ED8':'#e5e7eb'};transition:border-color 0.2s;" class="qv-thumb" onclick="document.getElementById('qvMainImg').src='${p.img}';document.querySelectorAll('.qv-thumb').forEach(el=>el.style.borderColor='#e5e7eb');this.style.borderColor='#1D4ED8'">
      <img src="${p.img}" style="width:100%;height:100%;object-fit:contain;padding:4px;" />
    </div>`;
  }
  document.getElementById('quickViewContent').innerHTML = `
    <div style="display:grid;grid-template-columns:1fr 1fr;min-height:460px;">
      <div style="padding:1.5rem;background:linear-gradient(145deg,#eef2ff,#fff,#f0f9ff);border-radius:1.5rem 0 0 1.5rem;">
        <div style="background:#fff;border-radius:1rem;height:280px;display:flex;align-items:center;justify-content:center;margin-bottom:12px;box-shadow:0 4px 16px rgba(29,78,216,0.08);">
          <img id="qvMainImg" src="${p.img}" style="width:100%;height:100%;object-fit:contain;padding:12px;" />
        </div>
        <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:8px;">${thumbs}</div>
      </div>
      <div style="padding:1.75rem;display:flex;flex-direction:column;">
        <span style="display:inline-block;font-size:0.68rem;font-weight:800;padding:4px 12px;border-radius:50px;text-transform:uppercase;margin-bottom:12px;${badge.color}">${badge.label}</span>
        <h2 style="font-family:Rajdhani,sans-serif;font-size:1.8rem;font-weight:700;color:#111827;margin-bottom:6px;">${p.name}</h2>
        <div style="color:#EAB308;margin-bottom:12px;">★★★★★ <span style="color:#9ca3af;font-size:0.85rem;">(128 reviews)</span></div>
        <div style="color:#1D4ED8;font-size:2rem;font-weight:800;margin-bottom:12px;font-family:Rajdhani,sans-serif;">PKR ${fmtPrice(p.price)}</div>
        <p style="color:#4b5563;font-size:0.875rem;line-height:1.7;margin-bottom:16px;">${p.desc}</p>
        <div style="display:flex;gap:8px;margin-bottom:20px;flex-wrap:wrap;">
          <span style="background:#eef2ff;color:#3730a3;font-size:0.75rem;font-weight:700;padding:6px 12px;border-radius:50px;"><i class="fas fa-cog"></i> ${p.engine}</span>
          <span style="background:#f0fdf4;color:#166534;font-size:0.75rem;font-weight:700;padding:6px 12px;border-radius:50px;"><i class="fas fa-gas-pump"></i> ${p.mileage}</span>
          <span style="background:#fff7ed;color:#c2410c;font-size:0.75rem;font-weight:700;padding:6px 12px;border-radius:50px;"><i class="fas fa-tachometer-alt"></i> ${p.speed}</span>
        </div>
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
          <span style="font-weight:600;color:#374151;font-size:0.9rem;">Qty:</span>
          <button class="qty-btn" onclick="qvQty=Math.max(1,qvQty-1);document.getElementById('qvQtyNum').textContent=qvQty">−</button>
          <span id="qvQtyNum" style="font-weight:700;min-width:28px;text-align:center;">1</span>
          <button class="qty-btn" onclick="qvQty++;document.getElementById('qvQtyNum').textContent=qvQty">+</button>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:auto;">
          <button onclick="addToCart(currentProduct.id,qvQty);closeQuickView();" style="border:2px solid #1D4ED8;color:#1D4ED8;background:transparent;border-radius:12px;padding:12px;font-weight:700;cursor:pointer;" onmouseover="this.style.background='#eff6ff'" onmouseout="this.style.background='transparent'">
            <i class="fas fa-cart-plus"></i> Add to Cart
          </button>
          <button onclick="addToCart(currentProduct.id,qvQty);closeQuickView();openCart();" style="background:#1D4ED8;color:#fff;border:none;border-radius:12px;padding:12px;font-weight:700;cursor:pointer;" onmouseover="this.style.background='#1e40af'" onmouseout="this.style.background='#1D4ED8'">
            Buy Now <i class="fas fa-arrow-right"></i>
          </button>
        </div>
      </div>
    </div>`;
  document.getElementById('quickViewModal').classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeQuickView() { document.getElementById('quickViewModal').classList.remove('open'); document.body.style.overflow = ''; }
```

### Order Modal + WhatsApp Submit

```js
function openOrderModal() {
  if (!cart.length) { showToast('Cart is empty!'); return; }
  const summary = document.getElementById('orderCartSummary');
  summary.innerHTML = '<div style="font-weight:700;margin-bottom:8px;">Order Summary</div>' +
    cart.map(i => `<div style="display:flex;justify-content:space-between;font-size:0.82rem;margin-bottom:4px;"><span>${i.name} × ${i.qty}</span><span style="font-weight:700;color:#1D4ED8;">PKR ${fmtPrice(i.price*i.qty)}</span></div>`).join('') +
    `<div style="border-top:1px solid #e5e7eb;margin-top:8px;padding-top:8px;display:flex;justify-content:space-between;font-weight:800;"><span>Total</span><span style="color:#1D4ED8;">PKR ${fmtPrice(cartTotal())}</span></div>`;
  closeCart();
  document.getElementById('orderModal').classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeOrderModal() { document.getElementById('orderModal').classList.remove('open'); document.body.style.overflow = ''; }

function submitOrder(e) {
  e.preventDefault();
  const fname = document.getElementById('oFname').value.trim();
  const lname = document.getElementById('oLname').value.trim();
  const city  = document.getElementById('oCity').value.trim();
  const addr  = document.getElementById('oAddress').value.trim();
  const wa    = document.getElementById('oWa').value.trim();
  const color = document.getElementById('oColor').value.trim() || 'Not specified';
  const notes = document.getElementById('oNotes').value.trim() || 'None';
  const items = cart.map(i => `• ${i.name} × ${i.qty} = PKR ${fmtPrice(i.price*i.qty)}`).join('\n');
  const msg = `🛵 *New ScootyPro Order!*\n\n*Items:*\n${items}\n\n*Total: PKR ${fmtPrice(cartTotal())}*\n\n*Customer:*\nName: ${fname} ${lname}\nCity: ${city}\nAddress: ${addr}\nWhatsApp: ${wa}\nColor: ${color}\nNotes: ${notes}\n\n💳 Payment: Cash on Delivery`;
  window.open('https://wa.me/923022311916?text=' + encodeURIComponent(msg), '_blank');
  cart = []; saveCart(); updateCartUI(); closeOrderModal();
  document.getElementById('orderForm').reset();
  showToast('Order placed! Check WhatsApp 🎉');
}
```

### Other JS Functions

```js
// Toast
function showToast(msg) {
  const ex = document.getElementById('toastEl');
  if (ex) ex.remove();
  const t = document.createElement('div');
  t.id = 'toastEl'; t.className = 'toast';
  t.innerHTML = '<i class="fas fa-check-circle" style="color:#4ade80;font-size:1.1rem;"></i> ' + msg;
  document.body.appendChild(t);
  setTimeout(() => { t.style.opacity='0'; t.style.transform='translateY(20px)'; t.style.transition='all 0.4s ease'; setTimeout(()=>t.remove(),400); }, 3000);
}

// Countdown (3 days from page load)
function startCountdown() {
  const end = new Date(); end.setDate(end.getDate() + 3);
  function tick() {
    const diff = Math.max(0, end - new Date());
    const d=Math.floor(diff/86400000), h=Math.floor((diff%86400000)/3600000), m=Math.floor((diff%3600000)/60000),
    s=Math.floor((diff%60000)/1000);
    const pad = n => String(n).padStart(2,'0');
    ['cdDays','cdHours','cdMins','cdSecs'].forEach((id,i)=>{const el=document.getElementById(id);if(el)el.textContent=pad([d,h,m,s][i]);});
  }
  tick(); setInterval(tick, 1000);
}

// Scroll reveal
function observeFadeUp() {
  const els = document.querySelectorAll('.fade-up:not([data-obs])');
  if (!els.length) return;
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); } });
  }, { threshold: 0.12 });
  els.forEach(el => { el.setAttribute('data-obs','1'); obs.observe(el); });
}

// Animated counters
function animateCounter(el) {
  const target = parseInt(el.dataset.target);
  const suffix = el.dataset.suffix || '';
  let current = 0; const steps = 60; const inc = target / steps;
  const timer = setInterval(() => {
    current = Math.min(current + inc, target);
    el.textContent = Math.floor(current) + suffix;
    if (current >= target) clearInterval(timer);
  }, 30);
}
function observeCounters() {
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting && !e.target.dataset.animated) { e.target.dataset.animated='1'; animateCounter(e.target); obs.unobserve(e.target); } });
  }, { threshold: 0.5 });
  document.querySelectorAll('.counter').forEach(el => obs.observe(el));
}

// FAQ
function toggleFaq(i) {
  const item = document.getElementById('faq-' + i);
  const body = item.querySelector('.faq-body');
  const isOpen = item.classList.contains('open');
  document.querySelectorAll('.faq-item').forEach(el => { el.classList.remove('open'); el.querySelector('.faq-body').style.maxHeight = '0'; });
  if (!isOpen) { item.classList.add('open'); body.style.maxHeight = body.scrollHeight + 'px'; }
}

// Header scroll
window.addEventListener('scroll', () => {
  document.getElementById('mainHeader').classList.toggle('header-scrolled', window.scrollY > 50);
});

// Mobile menu
function toggleMobileMenu() { document.getElementById('mobile-menu').classList.toggle('open'); }
function closeMobileMenu()  { document.getElementById('mobile-menu').classList.remove('open'); }

// Modal close on overlay click
document.getElementById('quickViewModal').addEventListener('click', e => { if (e.target === e.currentTarget) closeQuickView(); });
document.getElementById('orderModal').addEventListener('click', e => { if (e.target === e.currentTarget) closeOrderModal(); });

// Escape key
document.addEventListener('keydown', e => { if (e.key === 'Escape') { closeQuickView(); closeOrderModal(); closeCart(); } });

// INIT
document.addEventListener('DOMContentLoaded', () => {
  renderProducts(); updateCartUI(); startCountdown(); observeFadeUp(); observeCounters();
});
```

---

## STRICT RULES (MUST FOLLOW)

1. Single HTML file — NO external JS or CSS files
2. Product images: object-fit: CONTAIN always — never crop scooters
3. Gallery images: object-fit: CONTAIN always — never crop bikes
4. NO alert(), confirm(), or prompt() anywhere
5. Product grid: exactly 3 columns desktop, 2 tablet, 1 mobile
6. Cart: localStorage persistence (sp_cart key)
7. All 16 sections must be present and complete
8. WhatsApp number: +923022311916 everywhere
9. Hero: two-column layout desktop (text left, featured scooter card right)
10. All animations and JavaScript must be fully functional
11. Do NOT truncate the code — write the entire file completely