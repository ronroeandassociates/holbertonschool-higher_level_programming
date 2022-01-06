#!/usr/bin/node

/* script that prints My number: 
<first argument converted in integer> 
if the first argument can be converted to an 
integer */

const MyVar = process.argv[2];
if (isNaN(parseInt(MyVar)) === true) {
    console.log('Not a number');
} else {
    console.log('My number: ' + parseInt(MyVar));
}