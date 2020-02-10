#!/usr/bin/node
exports.esrever = function (list) {
  const revlist = [];
  for (let i = 0, j = list.length - 1; i < list.length; i++, j--) {
    revlist[i] = list[j];
  }
  return revlist;
};
