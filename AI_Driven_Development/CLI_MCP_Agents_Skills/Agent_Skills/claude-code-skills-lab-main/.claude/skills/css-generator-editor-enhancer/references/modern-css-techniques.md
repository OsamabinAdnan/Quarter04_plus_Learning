# Modern CSS Techniques Guide

## CSS Variables (Custom Properties)

CSS Variables allow you to define reusable values that can be changed in one place and applied throughout your stylesheet.

### Basic Usage
```css
:root {
  --primary-color: #007bff;
  --secondary-color: #6c757d;
  --font-size-base: 1rem;
  --border-radius: 0.25rem;
}

.button {
  background-color: var(--primary-color);
  font-size: var(--font-size-base);
  border-radius: var(--border-radius);
}
```

### Advanced Usage with Fallbacks
```css
.element {
  color: var(--text-color, #333); /* Uses #333 if --text-color is not defined */
  padding: var(--spacing, 1rem);
}
```

### Dynamic Changes with JavaScript
```javascript
// Change variable value with JavaScript
document.documentElement.style.setProperty('--primary-color', '#ff6b6b');
```

## Flexbox Layout

Flexbox is ideal for one-dimensional layouts (either rows or columns).

### Basic Flex Container
```css
.flex-container {
  display: flex;
  flex-direction: row; /* or column */
  justify-content: space-between; /* Horizontal alignment */
  align-items: center; /* Vertical alignment */
  flex-wrap: nowrap; /* or wrap */
}
```

### Flex Items
```css
.flex-item {
  flex: 1; /* grow, shrink, basis */
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: auto;
  align-self: auto; /* Override container align-items */
}
```

### Common Flexbox Patterns
```css
/* Center an element */
.center {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Space between items */
.space-between {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Equal width columns */
.equal-columns {
  display: flex;
}
.equal-columns > * {
  flex: 1;
}
```

## CSS Grid Layout

CSS Grid is perfect for two-dimensional layouts with both rows and columns.

### Basic Grid Container
```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 3 equal columns */
  grid-template-rows: auto; /* Rows adjust to content */
  gap: 1rem; /* Space between grid items */
}
```

### Grid Template Areas
```css
.layout {
  display: grid;
  grid-template-areas:
    "header header header"
    "sidebar main main"
    "footer footer footer";
  grid-template-columns: 200px 1fr 1fr;
  grid-template-rows: auto 1fr auto;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.footer { grid-area: footer; }
```

### Grid Item Placement
```css
.grid-item {
  grid-column: 1 / 3; /* Start at column 1, end at column 3 */
  grid-row: 1 / 2; /* Start at row 1, end at row 2 */

  /* Or shorthand */
  grid-area: 1 / 1 / 2 / 3;
}
```

## Responsive Design

### Media Queries
```css
/* Mobile first approach */
.component {
  padding: 1rem;
}

@media (min-width: 768px) {
  .component {
    padding: 2rem;
  }
}

@media (min-width: 1024px) {
  .component {
    padding: 3rem;
  }
}
```

### Container Queries (New)
```css
.card {
  display: grid;
  grid-template-areas: "img" "text";
  gap: 1em;
}

@container (min-width: 400px) {
  .card {
    grid-template-areas: "img text";
  }
}
```

## Logical Properties

Logical properties provide better support for internationalization by using flow-relative values.

```css
.text {
  /* Instead of margin-left/margin-right */
  margin-inline-start: 1rem;
  margin-inline-end: 1rem;

  /* Instead of padding-top/padding-bottom */
  padding-block-start: 1rem;
  padding-block-end: 1rem;

  /* Instead of text-align: left/right */
  text-align: start; /* or end */
}

/* Border logical properties */
.border-start {
  border-inline-start: 1px solid #ccc;
}
```

## Advanced Selectors

### Attribute Selectors
```css
/* Select elements with specific attributes */
input[type="email"] { border: 2px solid #007bff; }
a[href^="https://"] { color: #28a745; } /* Starts with */
a[href$=".pdf"] { color: #dc3545; } /* Ends with */
```

### Pseudo-class Selectors
```css
/* Select specific items */
li:first-child { font-weight: bold; }
li:last-child { border-bottom: none; }
li:nth-child(odd) { background-color: #f8f9fa; }

/* Select based on state */
input:focus { outline: 2px solid #007bff; }
input:disabled { opacity: 0.5; }
input:checked + label { color: #28a745; }
```

## Advanced Effects

### Advanced Box Shadows
```css
.elevated {
  box-shadow:
    0 1px 3px rgba(0,0,0,0.12),
    0 1px 2px rgba(0,0,0,0.24);
}

.card {
  box-shadow:
    0 2.8px 2.2px rgba(0, 0, 0, 0.02),
    0 6.7px 5.3px rgba(0, 0, 0, 0.028),
    0 12.5px 10px rgba(0, 0, 0, 0.035),
    0 22.3px 17.9px rgba(0, 0, 0, 0.042),
    0 41.8px 33.4px rgba(0, 0, 0, 0.05),
    0 100px 80px rgba(0, 0, 0, 0.07);
}
```

### Advanced Transforms
```css
.flip-card {
  perspective: 1000px;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.6s;
  transform-style: preserve-3d;
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
}
```

## Performance Considerations

### Efficient Animations
```css
/* Use transform and opacity for better performance */
.animated-element {
  transform: translateX(0);
  opacity: 1;
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.animated-element:hover {
  transform: translateX(10px);
  opacity: 0.8;
}

/* Avoid animating layout properties */
/* Don't animate: width, height, margin, padding, left, top, etc. */
```

### Containment
```css
/* Optimize rendering with containment */
.container {
  contain: layout style paint;
}
```

## Accessibility Features

### Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

/* Better approach - only apply animations when appropriate */
.button {
  color: #007bff;
  transition: color 0.2s ease;
}

@media (prefers-reduced-motion: no-preference) {
  .button:hover {
    color: #0056b3;
    transform: translateY(-2px);
    transition: all 0.2s ease;
  }
}
```

### High Contrast Mode
```css
@media (prefers-contrast: high) {
  .button {
    border: 2px solid;
  }
}