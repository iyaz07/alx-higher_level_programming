#!/usr/bin/node

exports.esrever = function (list) {
  const newlist = [];
  let x;

  for (x = list.length - 1; x >= 0; x--) {
    newlist.push(list[x]);
  }

  return (newlist);
};
