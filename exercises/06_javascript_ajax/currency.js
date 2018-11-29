
$(function () {
  var $currencies = $('#currencies');
  $.ajax({
    type:'GET',
    url:'http://data.fixer.io/api/latest?access_key=a9a648ff4113c91bddb8016c4b4cb605',
    success: function(currencies){
      $.each(currencies.rates, function(i, currency){

        $currencies.append('<tr><td>' + i + '</td><td>' + currency + '</td></tr>');

      })
      console.log('success', currencies.rates);

    }
  })

})

/*
    ? access_key = a9a648ff4113c91bddb8016c4b4cb605
    & base = JPY
    & symbols = USD,AUD,CAD,PLN,MXN  */
