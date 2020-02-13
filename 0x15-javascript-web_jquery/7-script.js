$.ajax({
  type: 'GET',
  url: 'https://swapi.co/api/people/5/?format=json',
  success: function(json) {
    console.log(json);
    console.log(json.name);
    $("#character").text(json.name);
  }
});
