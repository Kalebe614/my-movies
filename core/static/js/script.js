
btn_search = document.getElementById('search')//Get id btn_search
movie_name = document.getElementById('input-search')//Get movie name in the input field

//Send the name of the movie to filter
btn_search.addEventListener('click', function(e) {
    e.preventDefault()  
    window.location.href = '/?search='+movie_name.value
});
  