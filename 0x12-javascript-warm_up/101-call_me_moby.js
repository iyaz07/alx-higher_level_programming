#!/usr/bin/node

function callMeMoby (x, theFunction) {
  let y;
  for (y = 0; y < x; y++) {
    theFunction();
  }
}

module.exports.callMeMoby = callMeMoby;
