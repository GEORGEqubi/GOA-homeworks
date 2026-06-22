// 1) რა არის default პარამეტრი? გააკეთეთ შესაბამისი მაგალითი
// 2) const info = (name, age) => `my name is ${name}, i'm ${age} years old`
//    info('luka')
//    რას დააბრუნებს ეს კოდი?
// 3) კომენტარების სახით ახსენით რითი განსხვავდება function declaration და 
// function expression



// 1) default პარამეტრი არის ფუნქციის პარამეტრი რომელსაც აქვს ნაგულისხმევი მნიშვნელობა,


// მაგალითად: 

function greet(name = "Guest") {
    return `Hello, ${name}!`;
}
console.log(greet()); // Hello, Guest!


// 2) ეს კოდი დააბრუნებს "my name is luka, i'm undefined years old" რადგან age პარამეტრს არ აქვს
//  მნიშვნელობა და ის ავტომატურად ხდება undefined
 
// 3) function declaration არის ფუნქციის დეკლარაცია რომელიც იწყება სიტყვით function და მას აქვს სახელი
// Function Expression არის ფუნქცია რომელიც ინახება ცვლადში.
// function declaration
function add(a, b) {
    return a + b;
}
// function expression
const multiply = function(a, b) {
    return a * b;
};
console.log(multiply(3, 4)); // Output: 12