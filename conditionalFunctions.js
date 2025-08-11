/**
 * A function that mimics if-else-elif behavior using an array of conditions and actions.
 * 
 * @param {Array} conditions - An array of objects where each object contains:
 *                            - condition: A function that returns true/false
 *                            - action: A function to execute if condition is true
 * @returns The result of the first matching action, or undefined if no conditions match
 */
function matchCondition(conditions) {
    for (const { condition, action } of conditions) {
        if (condition()) {
            return action();
        }
    }
    return undefined;
}

/**
 * A function that mimics switch-case behavior.
 * 
 * @param {*} value - The value to match against
 * @param {Object} cases - An object where keys are values to match and values are functions to execute
 * @param {Function} defaultAction - A function to execute if no cases match (optional)
 * @returns The result of the matching case or default function
 */
function switchCase(value, cases, defaultAction = null) {
    if (value in cases) {
        return cases[value]();
    } else if (defaultAction) {
        return defaultAction();
    } else {
        return undefined;
    }
}

// Example usage:
// Example 1: Using matchCondition
const x = 10;

const result1 = matchCondition([
    { 
        condition: () => x < 0, 
        action: () => "Negative number" 
    },
    { 
        condition: () => x === 0, 
        action: () => "Zero" 
    },
    { 
        condition: () => x > 0 && x < 10, 
        action: () => "Positive single digit" 
    },
    { 
        condition: () => x >= 10, 
        action: () => "Positive double digit or larger" 
    }
]);

console.log(`Result 1: ${result1}`);

// Example 2: Using switchCase
const day = "Monday";

const result2 = switchCase(
    day,
    {
        "Monday": () => "Start of work week",
        "Friday": () => "End of work week",
        "Saturday": () => "Weekend!",
        "Sunday": () => "Weekend!"
    },
    () => "Regular day"
);

console.log(`Result 2: ${result2}`);

// Export functions for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        matchCondition,
        switchCase
    };
}