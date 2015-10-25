var canvas;  
var ctx;
var WIDTH = 600;
var HEIGHT = 600;
var scale = 10;

function init() {
  canvas = document.getElementById("canvas");
  ctx = canvas.getContext("2d");
  ctx.globalAlpha = 0.5;
}

function rect(color, x, y, w, h) {
  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.rect(x * scale, y * scale, w * scale - 1, h * scale - 1);
  ctx.closePath();
  ctx.fill();
}

function draw() {
  var start = 0;
  for (var i = 1; i <= 10; i++) {
    var color = (i % 2 == 0) ? "magenta" : "blue";
    for (var j = 0; j < i / 2; j++) {
      rect(color, start, i * j, i, i);    
      if (i * j != start) {
        rect(color, i * j, start, i, i);        
      }
    }
    start += i;
  }
}

init();
draw();