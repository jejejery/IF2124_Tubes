function getRectArea(width, height) {
    if (isNaN(width) || isNaN(height)) {
      throw 'lalala';
    }
  }
  
  try {
    getRectArea(3, 'A');
  } catch (e) {
    console.error(e);
    // expected output: "Parameter is not a number!"
  }