$(document).ready(function() {


    var userFeed = new Instafeed({
        get: 'user',
        userId: '1296617122',
        limit: 8,
        resolution: 'standard_resolution',
        accessToken: '1296617122.1677ed0.e7e348e5ef1f412c9bc2f2838f60a133',
        sortBy: 'most-recent',
        template: '<div class="col-lg-3 instaimg"><a href="{{image}}" title="{{caption}}" target="_blank"><img  src="{{image}}" alt="{{caption}}" class="img-fluid"/></a></div>',
    });


    userFeed.run();

    
    // This will create a single gallery from all elements that have class "gallery-item"
    $('.gallery').magnificPopup({
        type: 'image',
        delegate: 'a',
        gallery: {
            enabled: true
        }
    });


});
