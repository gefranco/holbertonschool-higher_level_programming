$.ajax({
  type: 'GET',
  url: 'https://swapi.co/api/people/5/?format=json',
  success: function(json) {
    console.log(json);
    results = json.results;
    $.each(results, function(i, title) {
      console.log(title);
    });
  }
});
