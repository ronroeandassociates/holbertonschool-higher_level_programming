#!/usr/bin/node

/* script that prints a message depending of the 
number of arguments passed */

let x = 0;
process.argv.forEach((_val, _index) => {
    x++;
});
if (x <= 2) {
    console.log('No argument');
} else if (x === 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}