#!/usr/bin/node
/**
 * Function that converts a number to another base.
 * @param {number} base - The new base
 * @returns {Function} - A funtion that converts a number to base
 */
exports.converter = function (base) {
  return num => num.toString(base);
}
