function keywordusage (text, keywords){

return "hello"
}


function frequencies(text,wordlist){
return "hello"
}


function rotate(array,steps){
  if(array.length < 2) {
      return array.slice(0);
    }

    var n = steps % array.length;

    if(n === 0) {
      return array.slice(0);
    }


    if(n < 0) {
      return array.slice(n).concat(array.slice(0, array.length+n));
    } else {
      return array.slice(n).concat(array.slice(0, n));
    }
  }



}
