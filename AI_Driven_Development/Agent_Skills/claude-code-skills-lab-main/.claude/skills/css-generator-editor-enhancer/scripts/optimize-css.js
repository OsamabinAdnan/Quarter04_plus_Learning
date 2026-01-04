#!/usr/bin/env node

/**
 * CSS Optimizer - Minifies and optimizes CSS for production
 *
 * This script removes unnecessary whitespace, comments, and optimizes
 * CSS for better performance.
 */

function minifyCSS(cssInput) {
  // Remove comments
  let minified = cssInput.replace(/\/\*[\s\S]*?\*\//g, '');

  // Remove unnecessary whitespace
  minified = minified
    .replace(/\s+/g, ' ') // Replace multiple spaces with single space
    .replace(/\s*([{}:;,>+~])\s*/g, '$1') // Remove space around CSS-specific characters
    .replace(/;\s*}/g, '}') // Remove semicolon before closing brace
    .replace(/\s*([({])\s*/g, '$1') // Remove space around parentheses
    .replace(/\s*([)}])\s*/g, '$1') // Remove space around parentheses
    .trim();

  return minified;
}

function optimizeSelectors(cssInput) {
  // Combine duplicate selectors
  const lines = cssInput.split('\n');
  const selectorMap = {};
  let currentSelector = '';
  let currentRules = [];

  lines.forEach(line => {
    line = line.trim();
    if (line.endsWith('{')) {
      // New selector block
      if (currentSelector && currentRules.length > 0) {
        // Save previous selector and rules
        if (!selectorMap[currentSelector]) {
          selectorMap[currentSelector] = [];
        }
        selectorMap[currentSelector] = [...selectorMap[currentSelector], ...currentRules];
      }

      currentSelector = line.replace('{', '').trim();
      currentRules = [];
    } else if (line === '}') {
      // End of selector block
      if (currentSelector && currentRules.length > 0) {
        if (!selectorMap[currentSelector]) {
          selectorMap[currentSelector] = [];
        }
        selectorMap[currentSelector] = [...selectorMap[currentSelector], ...currentRules];
      }
      currentSelector = '';
      currentRules = [];
    } else if (line && !line.startsWith('/*') && !line.endsWith('*/')) {
      // Rule inside selector
      currentRules.push(line);
    }
  });

  // Rebuild CSS with combined selectors
  let optimizedCSS = '';
  for (const [selector, rules] of Object.entries(selectorMap)) {
    optimizedCSS += `${selector} {\n`;
    // Remove duplicate rules
    const uniqueRules = [...new Set(rules)];
    uniqueRules.forEach(rule => {
      optimizedCSS += `  ${rule}\n`;
    });
    optimizedCSS += '}\n\n';
  }

  return optimizedCSS.trim();
}

function removeUnusedCSS(cssInput, htmlInput) {
  // This is a simplified version - a real implementation would be more complex
  // For now, just return the original CSS
  return cssInput;
}

function optimizeCSS(cssInput, options = {}) {
  let optimized = cssInput;

  if (options.minify) {
    optimized = minifyCSS(optimized);
  }

  if (options.optimizeSelectors) {
    optimized = optimizeSelectors(optimized);
  }

  if (options.removeUnused && options.html) {
    optimized = removeUnusedCSS(optimized, options.html);
  }

  return optimized;
}

// Example usage
function exampleUsage() {
  const sampleCSS = `
    /* This is a comment */
    .my-class {
      padding: 10px;
      margin: 5px;
      color: red;
    }

    .another-class {
      background: blue;
    }

    /* Another comment */
    .my-class {
      font-size: 16px;
    }
  `;

  console.log('Original CSS:');
  console.log(sampleCSS);
  console.log('\nMinified CSS:');
  console.log(minifyCSS(sampleCSS));
  console.log('\nOptimized CSS:');
  console.log(optimizeCSS(sampleCSS, { optimizeSelectors: true }));
}

// If this script is run directly, show an example
if (require.main === module) {
  console.log('CSS Optimizer - Minifies and optimizes CSS\n');
  exampleUsage();
}

module.exports = { minifyCSS, optimizeSelectors, removeUnusedCSS, optimizeCSS };