#!/usr/bin/node
// Import the dictionary from 101-data.js
const dict = require('./101-data').dict;

// Compute a new dictionary with occurrences as keys and user ids as values
const newDict = {};

for (const [userId, occurrences] of Object.entries(dict)) {
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(userId);
}

// Print the new dictionary
console.log(newDict);
