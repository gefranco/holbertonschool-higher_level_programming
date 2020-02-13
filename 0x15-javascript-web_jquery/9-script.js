$.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: function(json) {
    console.log(json);
    $("#hello").text(json.hello);
  }
});
