$.ajax({
  type: 'GET',
  url: 'https://swapi.co/api/films/?format=json',
  success: function(json) {
    console.log(json);
    results = json.results;
    $.each(results, function(i, title) {
      console.log(title);
    });
  }
});
