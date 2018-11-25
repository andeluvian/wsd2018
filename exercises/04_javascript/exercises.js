function keywordusage (text, keywords){
  var results =[];
  var split_text = text.split(" ");

  for(word in keywords){

    if(split_text.indexOf(word) > -1)
    {
      results.push("True")
    }
    else
    {
      results.push("False")
    }

  }
  return results
}


function frequencies(text,wordlist){
  var results = {};
  var sentence = text.split(" ");

  for(keyword in wordlist){
    results[keyword] = 0;

    var filter_sentence = sentence.filter(function(word)
    {

      if(keyword == word){
      return true;
      }
      else
      {

      return false;
      }


    }

  )


}


return results

}


function rotate(array, steps) {
    var removeArray = [];



    if (steps < 0)
        {var y = 0

        while (y > steps)
            {
            removeArray = array.splice(0, 1);
            var pos = array.length - 1;
            array.splice(pos, 0, removeArray[0]);


        y--;
        }
    }

    else
    {
      var x = 0
    while ( x < steps)
        {
        removeArray = array.splice(3, 1);
        array.splice(0, 0, removeArray[0]);
        x++;

        }


    }


    return array;

}











  /*if(array.length < 2) {
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

*/

}
