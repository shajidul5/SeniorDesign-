var car1;
var car2;
var car3;
var car4;
var car5;
var car6;
var color0;
var carColor;
function setup() {
createCanvas(700,700);
  // put setup code here
//width=700 h=500
frameRate(30);
car1=new Car();
car2=new Car();
car3=new Car();
car4=new Car();
car5=new Car();
car6=new Car();
color0=color(0,255,40);
carColor=color(255,0,0);
}

function draw() {
background(109, 162, 254);
fill(color0);
rect(0,height-70,70,70);
fill(7,60,255)
rect(width-70,0,70,70);
fill(0,0,0);
textSize(32);
text("Start",0,675)
text("End",width-70,50);
fill(carColor);
car1.move();
car1.display();
//car1.eyes();
car2.move();
car2.display();
car3.move();
car3.display();
car4.move();
car4.display();
car5.move();
car5.display();
car6.move();
car6.display();
}


function Car() {
this.x=random(10,35) //Math.floor((Math.random()*70)+20);
this.y=random(650,675) //Math.floor((Math.random()*height)+650);
this.Sw=width-10;
this.Sh=height-15;
this.width=10;
this.height=15;
this.speed=1;
this.dir1 = Math.floor((Math.random()*4)+0); //0=right 1=left 2=up 3=down 4=across
this.dummy=0;
this.randmove=Math.floor((Math.random()*300)+60);
this.count=0;
this.move = function() {
if(this.count>this.randmove) { this.count=0; this.dir1 = Math.floor((Math.random()*4)+0);  }
if(this.dir1==0) {
this.x += 1; 
if(this.x>this.Sw ){
this.dir1=Math.floor((Math.random()*4)+0);
}
 }
else if(this.dir1==1){
this.x -= 1; if(this.x<0){ this.dir1=Math.floor((Math.random()*4)+0);
//if(this.dir1==1) {this.dir1=0;  }
}} 
else if(this.dir1==2){ 
this.y -= 1; if(this.y<0) {this.dir1=Math.floor((Math.random()*4)+0); 
//if(this.dir==2) {this.dir2=3;}
  } }
else if(this.dir1==3){
this.y += 1; if(this.y>this.Sh) {this.dir1=Math.floor((Math.random()*4)+0);} 
 }
this.count+=4;
} 

this.display=function(){
if(this.dir1==3 || this.dir1==2) 
rect(this.x,this.y,this.width,this.height);
else {   
rect(this.x,this.y,this.height,this.width);
}} 
}

