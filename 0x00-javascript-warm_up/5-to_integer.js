#!/usr/bin/node
const MyVar = process.argv[2];
if (isNaN(parseInt(MyVar)) === true) {
    console.log('Not a number');
} else {
    console.log('My number: ' + parseInt(MyVar));
}
