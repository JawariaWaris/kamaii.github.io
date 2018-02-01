/* ==============================================
 Website Preloader
 =============================================== */

$(window).on("load",function() {
    'use strict';
    // Animate loader off screen
    $(".se-pre-con").fadeOut( "slow" );

});


/* ==============================================
 Calling Scroll Animations
 =============================================== */
'use strict';
AOS.init();


/* ==============================================
 Navigation Fixed on Scroll
 =============================================== */


/* ==============================================
 Navigation Click & Active on Reaching Section
 =============================================== */





$(document).ready(function() {

    /* ==============================================
     Testimonial Carousel
     =============================================== */
    $("#testimonial").owlCarousel({
        autoPlay: 4000, //Set AutoPlay to 4 seconds
        items : 3,
        itemsDesktop : [1199,3],
        itemsDesktopSmall : [979,2],
        itemsMobile : [500,1]
    });


    /* =============================================
     Banner Carousel
     ==============================================*/
    $(".owl-carousel2").owlCarousel({
        items: 1,
        autoPlay: 4000, //Set AutoPlay to 4 seconds
        stopOnHover: false,
        loop:true,
        transitionStyle : "fade",
        pagination:false,
        nav:false
    });

    /* ==============================================
     Accordian used in "What we can offer?" Section
     =============================================== */
    'use strict';
    var acordian = $(".acordian");
    $(acordian).on('click',function(){
        'use strict';
        if($(this).hasClass('active')){
            $(this).toggleClass('active')
        }
        else{
            $(acordian).removeClass('active');
            $(this).addClass('active');
        }
    });


    /* ==============================================
     Calling Nice Scroll
     =============================================== */
    'use strict';
    $("html").niceScroll();

});


/* ==============================================
 Scroll Back To Top
 =============================================== */


function topFunction() {
    $('body,html').animate({
        scrollTop: 0
    }, 1500);
}



/* ==============================================
 Why Choose us Video Animation | Youtube Link Video
 =============================================== */

