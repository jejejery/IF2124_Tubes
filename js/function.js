function do_something(x) {
    // This is a sample comment
    while(x < 1){
      x++;
      if(x == 3){
        break;
      }
    }
    switch(x+2){
      case 1:
        x -= 11;
        break;
      case 2:
        console.log('2');
        break;
    }
  }

