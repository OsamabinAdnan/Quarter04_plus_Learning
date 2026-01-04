# CSS Property Reference Guide

## Layout Properties

### Display
- `display: block` - Elements take up full width and start on new lines
- `display: inline` - Elements flow within text, only take up necessary width
- `display: inline-block` - Combines inline flow with block formatting
- `display: flex` - Creates flexible box layout container
- `display: grid` - Creates grid layout container
- `display: none` - Hides element completely

### Positioning
- `position: static` - Default positioning
- `position: relative` - Positioned relative to normal position
- `position: absolute` - Positioned relative to nearest positioned ancestor
- `position: fixed` - Positioned relative to viewport
- `position: sticky` - Switches between relative and fixed based on scroll

### Flexbox Properties
- `flex-direction` - Direction of flex items (row, column, row-reverse, column-reverse)
- `justify-content` - Alignment along main axis (flex-start, center, flex-end, space-between, space-around)
- `align-items` - Alignment along cross axis (flex-start, center, flex-end, stretch)
- `flex-wrap` - Whether flex items wrap (nowrap, wrap, wrap-reverse)
- `flex` - Shorthand for flex-grow, flex-shrink, and flex-basis

### Grid Properties
- `grid-template-columns` - Defines columns in grid
- `grid-template-rows` - Defines rows in grid
- `grid-template-areas` - Defines named grid areas
- `grid-gap` - Space between grid items
- `justify-items` - Alignment of grid items along inline axis
- `align-items` - Alignment of grid items along block axis
- `justify-content` - Alignment of entire grid along inline axis
- `align-content` - Alignment of entire grid along block axis

## Typography Properties

### Font Properties
- `font-family` - Font face(s) to use
- `font-size` - Size of text
- `font-weight` - Weight of text (normal, bold, 100-900)
- `font-style` - Style of text (normal, italic, oblique)
- `font-variant` - Variant of font (normal, small-caps)

### Text Properties
- `text-align` - Horizontal alignment of text
- `text-decoration` - Decorative lines on text
- `text-transform` - Capitalization of text
- `line-height` - Height of text lines
- `letter-spacing` - Spacing between letters
- `word-spacing` - Spacing between words
- `text-shadow` - Shadow effect on text

## Color and Background Properties

### Color
- `color` - Text color
- `background-color` - Background color
- `opacity` - Transparency level (0-1)

### Background
- `background-image` - Background image
- `background-repeat` - How background image repeats
- `background-position` - Position of background image
- `background-size` - Size of background image
- `background-attachment` - Scroll behavior of background

## Spacing Properties

### Margin
- `margin-top`, `margin-right`, `margin-bottom`, `margin-left` - Individual margins
- `margin` - Shorthand for all margins
  - `margin: 10px` - All sides
  - `margin: 10px 20px` - Vertical, Horizontal
  - `margin: 10px 20px 15px` - Top, Horizontal, Bottom
  - `margin: 10px 20px 15px 25px` - Top, Right, Bottom, Left

### Padding
- `padding-top`, `padding-right`, `padding-bottom`, `padding-left` - Individual padding
- `padding` - Shorthand for all padding (same pattern as margin)

## Border Properties

### Border Width
- `border-width` - Width of border
- `border-top-width`, `border-right-width`, etc. - Individual border widths

### Border Style
- `border-style` - Style of border (solid, dashed, dotted, etc.)
- `border-top-style`, `border-right-style`, etc. - Individual border styles

### Border Color
- `border-color` - Color of border
- `border-top-color`, `border-right-color`, etc. - Individual border colors

### Border Shorthand
- `border` - Combines width, style, and color
- `border-top`, `border-right`, etc. - Individual border shorthand

## Sizing Properties

### Width and Height
- `width`, `height` - Dimensions of element
- `min-width`, `min-height` - Minimum dimensions
- `max-width`, `max-height` - Maximum dimensions

### Box Sizing
- `box-sizing` - How width/height are calculated (content-box, border-box)

## Effects Properties

### Border Radius
- `border-radius` - Rounded corners
- `border-top-left-radius`, etc. - Individual corner rounding

### Box Shadow
- `box-shadow` - Shadow effect on element
  - Format: `h-offset v-offset blur spread color inset`

### Transform
- `transform` - Transform element (rotate, scale, translate, skew)
- `transform-origin` - Point for transformations

### Transition
- `transition` - Smooth transitions between property changes
  - Format: `property duration timing-function delay`

### Animation
- `animation` - Apply keyframe animations
- `@keyframes` - Define animation keyframes

## Modern CSS Features

### CSS Custom Properties (Variables)
- `--property-name: value` - Define custom property
- `var(--property-name, fallback)` - Use custom property

### Logical Properties
- `margin-block-start`, `margin-block-end` - Block axis margins
- `margin-inline-start`, `margin-inline-end` - Inline axis margins
- `padding-block-start`, `padding-inline-start`, etc. - Logical padding
- `border-block-start`, `border-inline-start`, etc. - Logical borders

### Container Queries (New)
- `@container` - Style based on container size

### Color Functions
- `rgb(r, g, b)` - Red, green, blue values
- `rgba(r, g, b, a)` - RGB with alpha
- `hsl(h, s, l)` - Hue, saturation, lightness
- `hsla(h, s, l, a)` - HSL with alpha
- `color-mix()` - Mix colors (new)

## Responsive Units

### Absolute Units
- `px` - Pixels
- `pt` - Points
- `cm` - Centimeters
- `mm` - Millimeters
- `in` - Inches

### Relative Units
- `em` - Relative to font size of element
- `rem` - Relative to root font size
- `%` - Percentage of parent
- `vw` - 1% of viewport width
- `vh` - 1% of viewport height
- `vmin` - 1% of smaller viewport dimension
- `vmax` - 1% of larger viewport dimension
- `fr` - Fraction of available space (grid)

## Pseudo-classes and Pseudo-elements

### Pseudo-classes
- `:hover`, `:active`, `:focus` - Interaction states
- `:first-child`, `:last-child`, `:nth-child()` - Positional states
- `:not()`, `:empty`, `:target` - Conditional states
- `:checked`, `:disabled`, `:enabled` - Form states

### Pseudo-elements
- `::before`, `::after` - Generate content
- `::first-line`, `::first-letter` - Target specific parts
- `::selection` - Target selected text