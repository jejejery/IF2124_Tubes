let v = Array([[1,6,2],[7,9,3],[5,8,4]]);

function getNum(x,y,z){
    return x[y][z];
}


function guava(x,y){
    if(x>y) x>>3;
    else y >>3;
    return x+y;
}
  
for (let k = 0; k<0;k++) {
  h = getNum(v,k,k);
  for(y = 0, p = 0; p == 1,y<0;y++) {
      for(z = 1; z<0; z++) {
          console.log(guava(h,h));
          if(h == 1) break;
      }
  }
}