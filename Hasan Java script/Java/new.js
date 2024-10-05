var hasan='mehedi'
//console.log("hasan")
var b=34
console.log('mozumder '+b) 
var accountNumber=12223
console.log(accountNumber)
var num=Number('6677')
console.log(num)
var Num=23.32
console.log(Number.parseInt(Num))
console.log(Number.parseFloat(num))
console.log(1/0)
var abc
var xyz = null
console.log(null)
console.log(abc)
var num1='1000'
var num2=5
console.log(num1*num2)
//falsy values
''
0
null
NaN
undefined
console.log(Boolean(''))
console.log(Boolean(null))
console.log(Boolean(1))
//Hexadecimal number
var hex =0xff
console.log(hex)
var oct = 0734
console.log(oct)
//Operator
var a=10
var b=3
console.log(a%b)
//pre or post increament
console.log(a++)
console.log(++b)
//Ternary operator
c=(a>b)?a:b
console.log(c)
//comparison operator
a+=b
console.log(a)
a/=b
console.log(a)
console.log(a==b)
console.log(a!=b)
console.log(a>b)
console.log(a<b)
console.log(a>=b)
console.log(a<=b)
c=20
d='20'
e=15
console.log(c===d)
//Logical operator
//&&
//||
//!
console.log(typeof c)
console.log(typeof d)
//JS math
console.log(Math.E)
var n=3.5322
console.log(Math.abs(n))
console.log(Math.floor(n))
console.log(Math.ceil(n))
console.log(Math.round(n))
console.log(Math.max(400,5000,300))
console.log(Math.min(300,2333))
console.log(Math.pow(2,3))
console.log(Math.sqrt(9))
console.log(Math.random())
console.log(Math.round(Math.random()*50+5))

/*Date
and time
*/
var date=new Date()
console.log(date)
console.log(date.toDateString())
console.log(date.toTimeString())
console.log(date.toLocaleString())
console.log(date.getFullYear())
console.log(date.getMonth())
console.log(date.getDate())
console.log(date.getHours())

var a=10
var b=20
if(a<b){
    console.log(a+' is greter than '+b)
}
else{
    console.log(b+' is greater than '+a)
}
var n=28
if(n%2==0){
    console.log('n is even number')
}
else if(n%2!=0){
    console.log('n is odd number')
}
else{
    console.log('n is a compound number')
}
var a=43345
var b=22333
var c=3222
if(a>b && a>c){
    console.log(a)
}
else if(b>a && b>c){
    console.log(b)
}
else{
    console.log(c)
}
var a=433
var b=22333
var c=3222
if(a>b || a>c){
    console.log(a)
}
else if(b>a || b>c){
    console.log(b)
}
else{
    console.log(c)
}
var a=10
var b=20
var c=27
var check=!(a>b)
console.log(check)
var c=(a>b)?(a>c?a:c):(b>c?b:c)
console.log(c)

//for(i=0;i<20;i++){
 //   console.log((i+1)' mehedi hasan')
//}












