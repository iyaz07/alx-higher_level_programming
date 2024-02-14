#!/usr/bin/node

// Returns the number of occurrences of an element in a list

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let i = 0; list[i]; i++) {
    if (list[i] === searchElement) {
      counter++;
    }
  }
  return counter;
};
