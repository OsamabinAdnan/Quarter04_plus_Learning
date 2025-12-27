#!/usr/bin/env node

/**
 * CSS Enhancer - Adds modern CSS features to existing CSS
 *
 * This script enhances CSS with modern features like CSS variables,
 * flexbox, grid, and other contemporary CSS capabilities.
 */

function addCSSVariables(cssInput, variables = {}) {
  // Default color variables
  const defaultVariables = {
    '--primary-color': '#007bff',
    '--secondary-color': '#6c757d',
    '--success-color': '#28a745',
    '--info-color': '#17a2b8',
    '--warning-color': '#ffc107',
    '--danger-color': '#dc3545',
    '--light-color': '#f8f9fa',
    '--dark-color': '#343a40',
    '--font-size-base': '1rem',
    '--border-radius': '0.25rem',
    '--box-shadow': '0 0.125rem 0.25rem rgba(0, 0, 0, 0.075)',
    '--transition': 'all 0.2s ease-in-out'
  };

  // Merge provided variables with defaults
  const allVariables = { ...defaultVariables, ...variables };

  // Create CSS variable declaration block
  let variableBlock = ':root {\n';
  for (const [name, value] of Object.entries(allVariables)) {
    variableBlock += `  ${name}: ${value};\n`;
  }
  variableBlock += '}\n\n';

  // Replace color values with CSS variables where appropriate
  let enhancedCSS = cssInput;
  for (const [name, value] of Object.entries(allVariables)) {
    if (name.includes('color')) {
      // Replace hex colors
      enhancedCSS = enhancedCSS.replace(new RegExp(value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g'), name);
    }
  }

  // Add the variable block to the beginning of the CSS
  return variableBlock + enhancedCSS;
}

function convertToFlexbox(cssInput) {
  // Look for common layout patterns and convert to flexbox
  let enhancedCSS = cssInput;

  // Convert float-based layouts to flexbox
  enhancedCSS = enhancedCSS.replace(/float\s*:\s*left\s*;/g, 'display: flex; flex-direction: row;');
  enhancedCSS = enhancedCSS.replace(/float\s*:\s*right\s*;/g, 'display: flex; justify-content: flex-end;');
  enhancedCSS = enhancedCSS.replace(/float\s*:\s*none\s*;/g, 'flex: none;');

  // Add flexbox container properties
  enhancedCSS = enhancedCSS.replace(/display\s*:\s*block\s*;/g, 'display: flex; flex-direction: column;');

  return enhancedCSS;
}

function convertToGrid(cssInput) {
  // Look for common layout patterns and convert to CSS Grid
  let enhancedCSS = cssInput;

  // Identify potential grid containers and add grid properties
  enhancedCSS = enhancedCSS.replace(/display\s*:\s*block\s*;/g, 'display: grid;');

  // Look for patterns that suggest grid layout (multiple direct children)
  // This is a simplified version - a real implementation would be more sophisticated
  const gridPatterns = [
    /\.container\s*\{/,
    /\.row\s*\{/,
    /\.col\s*\{/
  ];

  gridPatterns.forEach(pattern => {
    enhancedCSS = enhancedCSS.replace(pattern, (match) => {
      if (!match.includes('grid') && !match.includes('flex')) {
        return match.replace('{', '{\n  display: grid;');
      }
      return match;
    });
  });

  return enhancedCSS;
}

function addModernFeatures(cssInput, options = {}) {
  let enhancedCSS = cssInput;

  // Add CSS variables if requested
  if (options.addVariables) {
    enhancedCSS = addCSSVariables(enhancedCSS, options.variables || {});
  }

  // Convert to flexbox if requested
  if (options.convertToFlexbox) {
    enhancedCSS = convertToFlexbox(enhancedCSS);
  }

  // Convert to grid if requested
  if (options.convertToGrid) {
    enhancedCSS = convertToGrid(enhancedCSS);
  }

  // Add modern units and properties
  if (options.modernizeUnits) {
    // Replace common pixel values with rem/em where appropriate
    enhancedCSS = enhancedCSS.replace(/\b(\d*\.?\d+)px\b/g, (match, value) => {
      // Convert common font sizes to rem
      if (value >= 12 && value <= 24) {
        return `${(value / 16).toFixed(2)}rem`;
      }
      return match;
    });
  }

  // Add logical properties for internationalization
  if (options.addLogicalProperties) {
    enhancedCSS = enhancedCSS.replace(/margin-left/g, 'margin-inline-start');
    enhancedCSS = enhancedCSS.replace(/margin-right/g, 'margin-inline-end');
    enhancedCSS = enhancedCSS.replace(/padding-left/g, 'padding-inline-start');
    enhancedCSS = enhancedCSS.replace(/padding-right/g, 'padding-inline-end');
    enhancedCSS = enhancedCSS.replace(/text-align:\s*left/g, 'text-align: start');
    enhancedCSS = enhancedCSS.replace(/text-align:\s*right/g, 'text-align: end');
  }

  // Add prefers-reduced-motion media queries
  if (options.addReducedMotion) {
    // Find animations and transitions, wrap them in reduced motion queries
    const animationRegex = /animation:\s*([^;]+);/g;
    const transitionRegex = /transition:\s*([^;]+);/g;

    enhancedCSS = enhancedCSS.replace(animationRegex, (match) => {
      return `@media (prefers-reduced-motion: no-preference) {\n  ${match}\n}`;
    });

    enhancedCSS = enhancedCSS.replace(transitionRegex, (match) => {
      return `@media (prefers-reduced-motion: no-preference) {\n  ${match}\n}`;
    });
  }

  return enhancedCSS;
}

// Example usage
function exampleUsage() {
  const sampleCSS = `
    .container {
      width: 100%;
      padding: 15px;
    }

    .header {
      background-color: #007bff;
      color: #ffffff;
      padding: 20px;
    }

    .nav {
      float: left;
      width: 200px;
    }

    .content {
      float: right;
      width: calc(100% - 220px);
      padding: 10px;
    }

    .button {
      background-color: #007bff;
      color: #ffffff;
      padding: 10px 15px;
      border-radius: 4px;
      transition: all 0.3s ease;
    }
  `;

  console.log('Original CSS:');
  console.log(sampleCSS);

  const enhancedCSS = addModernFeatures(sampleCSS, {
    addVariables: true,
    convertToFlexbox: true,
    modernizeUnits: true,
    addLogicalProperties: true,
    addReducedMotion: true
  });

  console.log('\nEnhanced CSS with modern features:');
  console.log(enhancedCSS);
}

// If this script is run directly, show an example
if (require.main === module) {
  console.log('CSS Enhancer - Adds modern CSS features to existing CSS\n');
  exampleUsage();
}

module.exports = {
  addCSSVariables,
  convertToFlexbox,
  convertToGrid,
  addModernFeatures,
  defaultVariables: {
    '--primary-color': '#007bff',
    '--secondary-color': '#6c757d',
    '--success-color': '#28a745',
    '--info-color': '#17a2b8',
    '--warning-color': '#ffc107',
    '--danger-color': '#dc3545',
    '--light-color': '#f8f9fa',
    '--dark-color': '#343a40',
    '--font-size-base': '1rem',
    '--border-radius': '0.25rem',
    '--box-shadow': '0 0.125rem 0.25rem rgba(0, 0, 0, 0.075)',
    '--transition': 'all 0.2s ease-in-out'
  }
};