$(document).ready(function() {

    // getting user input
    var city;
    var country;

    console.log(city)

    $('#go').click(function() {
      city = $('#city').val();
    });

    if ($('#city').val() != undefined) {
      var city = $('#city').val()
      console.log(city)
      var url = "http://api.openweathermap.org/data/2.5/weather?q="
      var key = "2c03335f9552691480c68fd9bc03d907";
      var request = new XMLHttpRequest();
      request.open("GET",url + city + "&appid=" + key, false);
      request.send();

      // parsing json data
      var json = JSON.parse(request.responseText);

      // Writing data
      var temp = (parseFloat(json.main.temp) - 273.15).toFixed(1);

      $('#temp').text(temp + "°C");
      $('#desc').text(json.weather[0].description);

    }

    //TODO:$('#desc').text(json.weather[0].icon);
});
