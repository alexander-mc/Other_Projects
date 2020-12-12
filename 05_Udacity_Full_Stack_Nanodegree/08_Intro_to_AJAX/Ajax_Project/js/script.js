
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text(""); 

    // load streetview
    var streetStr = $('#street').val();
    var cityStr = $('#city').val();
    var address = streetStr + ', ' + cityStr;
    var streetviewUrl = 'http://maps.googleapis.com/maps/api/streetview?size=600x300&location=' + address + '';  

    $greeting.text('So, you want to live at ' + address + '?'); 
    $body.append('<img class="bmgimg" src="' + streetviewUrl + '">');
    
    // NYTimes AJAX request

    var nytimesUrl = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q='
        + cityStr
        + '&sort=newest&api-key=310eee2963be4694b430b415509c2e9f';

    $.getJSON(nytimesUrl, function(data){
        // in the above, the request is the first argument that is passed (the url) and the response from the site is passed through the second argumet (data)
        $nytHeaderElem.text('New York Times Articles About ' + cityStr);

        articles = data.response.docs;
        for (var i = 0; i < articles.length; i++) {
        // above means "set i equal to 0, keep going until you have cycled through all the data, increasing i by 1 after each iteration")
            var article = articles[i];
            $nytElem.append('<li class="article">' + 
                '<a href="' + article.web_url + '">'+article.headline.main+
                    '</a>'+
                '<p>' + article.snippet + '</p>' +
            '</li>');
        };

    }).error(function(e){
        $nytHeaderElem.text('New York Times Articles Could Not Be Loaded');
    });


    //the following wikipedia api does not support CORS
    // (whereas the above does().
    // Thus, the more robust ajax needs to be used (actually, the jQuery.get)() function is an abstraction of the jQuery.ajax() method). That is, the above code for the nytimes api could have also used ajax).
    // The below uses JSONP, rather than CORS
    // However, error handing is NOT built into JSONP

    var wikiUrl = 'http://en.wikipedia.org/w/api.php?action=opensearch&search='
        + cityStr
        + '&format=json&callback=wikiCallback';

    // Build error handling into JSONP
    // setTimeout stops the request if it runs for too long
    // Text is set up to show after 8000ms, or 8 seconds

    var wikiRequestTimeout = setTimeout(function(){
        $wikiElem.text("failed to get wikipedia resources");
    }, 8000);

    $.ajax({
        url: wikiUrl,
        dataType: "jsonp",
        // jsonp: "callback"
        success: function ( response ) {
            var articleList = response[1];

            for (var i = 0; i < articleList.length; i++) {
                articleStr = articleList[i];
                var url = 'http://en.wikipedia.org/wiki/'
                    + articleStr;
                $wikiElem.append('<li><a href="' + url + '">'
                    + articleStr + '</a></li>');
            };

            clearTimeout(wikiRequestTimeout);
            // above stops timeout, as we don't need it (the request was successful)
        }
    });

    return false;

};

$('#form-container').submit(loadData);
