#!/usr/bin/node
/**
 * Function that logs the number of arguments already printed
 * and the new argument value.
 * @param {*} item - The current argument value to print.
 */
let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
