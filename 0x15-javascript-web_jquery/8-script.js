$.ajax({
  type: 'GET',
  url: 'https://swapi.co/api/films/?format=json',
  success: function(json) {
    console.log(json);
    results = json.results;
    $.each(results, function(i, movie) {
      console.log(movie.title);
      $("#list_movies").append(movie.title);
    });
  }
});
