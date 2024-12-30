#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const uniqueSortedArgs = [...new Set(args)].sort((a, b) => b - a);
  console.log(uniqueSortedArgs[1] || 0);
}
