$('#currency').submit(function(e) {

e.preventDefault();

var date = new Date($('#date').val());
day = date.getDate();
month = date.getMonth() + 1;
year = date.getFullYear();

  var $currencies = $('#currencies');




  $.ajax({
    type:'GET',
    url:'http://acos.cs.hut.fi/wsd-currency/'+ year+'-'+month+'-'+day ,
    crossDomain:true,
    jsonpCallback:"example",
    dataType:"jsonp",

    success: function(currencies){
      $.each(currencies, function(i, currency){
        $currencies.append('<tr><td>' + i + '</td><td>' + currency + '</td></tr>');
      });
    }
  });
});
$('#search').on('click', function(){
  var date = new Date($('#date').val());
  day = date.getDate();
  month = date.getMonth() + 1;
  year = date.getFullYear();
//  alert([day, month, year].join('-'));

});
