#!/usr/bin/node

exports.converter = function (base) {
  return function (base2) {
    return parseInt(base2).toString(base);
  };
};
