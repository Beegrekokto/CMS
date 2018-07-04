jQuery(document).on('ready', function ($) {

    "use strict";


    /*---------------------------

        SEARCH BOX

    ----------------------------*/

    jQuery('.search-box').on('click', function () {

        jQuery('.search-form').slideToggle();

    });


    /*--------------------------

        STICKY MAINMENU

    ---------------------------*/

    $("#mainmenu-area").sticky({

        topSpacing: 0

    });


    /*---------------------------

        SMOOTH SCROLL

    -----------------------------*/

    $('ul#nav li a[href^="#"], a.navbar-brand, a.scrolltotop').on('click', function (event) {

        var id = $(this).attr("href");

        var offset = 60;

        var target = $(id).offset().top - offset;

        $('html, body').animate({

            scrollTop: target

        }, 1500, "easeInOutExpo");

        event.preventDefault();

    });


    /*----------------------------

        MOBILE & DROPDOWN MENU

    ------------------------------*/

    jQuery('.stellarnav').stellarNav({

        theme: 'dark'

    });


    /*----------------------------

        SCROLL TO TOP

    ------------------------------*/

    $(window).scroll(function () {

        var totalHeight = $(window).scrollTop();

        if (totalHeight > 300) {

            $(".scrolltotop").fadeIn();

        } else {

            $(".scrolltotop").fadeOut();

        }

    });


    /*--------------------------

       HOME PARALLAX BACKGROUND

    ----------------------------*/

    $(window).stellar({

        responsive: true,

        positionProperty: 'position',

        horizontalScrolling: false

    });


    /*---------------------------

        HOME SLIDER

    -----------------------------*/

    var $homeSlider = $('.welcome-slider-area');

    $homeSlider.owlCarousel({

        merge: true,

        smartSpeed: 2000,

        loop: false,

        nav: false,

        navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],

        autoplay: false,

        autoplayTimeout: 5000,

        mouseDrag: false,

        touchDrag: false,

        margin: 0,

        animateIn: 'fadeIn',

        animateOut: 'fadeOut',

        responsiveClass: true,

        responsive: {

            0: {

                items: 1

            },

            600: {

                items: 1

            },

            1000: {

                items: 1

            },

            1200: {

                items: 1

            }

        }

    });


    /*------------------------------

        TESTMONIAL SLIDER

    -------------------------------*/

    var client_photo2 = $('.client_details');

    client_photo2.owlCarousel({

        loop: true,

        margin: 20,

        autoplay: false,

        dots: true,

        autoplayTimeout: 4000,

        smartSpeed: 600,

        responsive: {

            0: {

                items: 1

            },

            600: {

                items: 1

            },

            992: {

                items: 1

            }

        }

    });


    var client_photo = $('.client_photo');

    client_photo.owlCarousel({

        loop: true,

        margin: 0,

        dots: true,

        autoplayTimeout: 4000,

        smartSpeed: 600,

        mouseDrag: true,

        touchDrag: false,

        center: true,

        responsive: {

            0: {

                items: 1

            },

            600: {

                items: 2

            },

            992: {

                items: 3

            }

        }

    });

    $('.client_nav .testi_next').on('click', function () {

        client_photo.trigger('next.owl.carousel');

    });

    $('.client_nav .testi_prev').on('click', function () {

        client_photo.trigger('prev.owl.carousel');

    });


    client_photo.on('translate.owl.carousel', function (property) {

        $('.client-details-content .owl-dot:eq(' + property.page.index + ')').click();

    });

    client_photo2.on('translate.owl.carousel', function (property) {

        $('.client-photo-list .owl-dot:eq(' + property.page.index + ')').click();

    });


    /*------------------------------

        CLIENT SLIDER

    -------------------------------*/

    var client_list = $('.client-list');

    client_list.owlCarousel({

        loop: true,

        center: true,

        margin: 5,

        dots: true,

        autoplayTimeout: 4000,

        smartSpeed: 600,

        mouseDrag: true,

        touchDrag: false,

        responsive: {

            0: {

                items: 1

            },

            600: {

                items: 3

            },

            992: {

                items: 5

            }

        }

    });

    $('.client_nav_1 .testi_next').on('click', function () {

        client_list.trigger('next.owl.carousel');

    });

    $('.client_nav_1 .testi_prev').on('click', function () {

        client_list.trigger('prev.owl.carousel');

    });


    /*------------------------------

        Services SLIDER

    -------------------------------*/


    var all_blog = $('.all_blog');

    all_blog.owlCarousel({

        loop: true,

        center: true,

        margin: 20,

        dots: true,

        autoplayTimeout: 4000,

        smartSpeed: 600,

        mouseDrag: true,

        touchDrag: false,
        responsive: {

            0: {

                items: 1

            },

            600: {

                items: 3

            },

            992: {

                items: 3

            }

        }

    });

    $('.services_nav .testi_next').on('click', function () {

        all_blog.trigger('next.owl.carousel');

    });

    $('.services_nav .testi_prev').on('click', function () {

        all_blog.trigger('prev.owl.carousel');

    });

    /*----------------------------

        TAB PANEL ACTIVE

    ------------------------------*/

    $('.panel').on('click', function (e) {

        $('.panel').removeClass('active');

        var $this = $(this);

        if (!$this.hasClass('active')) {

            $this.addClass('active');

        }

        e.preventDefault();

    });


    /*--------------------------

        ACTIVE WOW JS

    ----------------------------*/

    new WOW().init();


}(jQuery));


jQuery(window).on('load', function () {

    "use strict";

    /*--------------------------

        PRE LOADER

    ----------------------------*/

    $(".preeloader").fadeOut(1000);


});

/*--------------------------

    Gallery photo slider

----------------------------*/

var gallery_photo = $('.gallery_photo_1');

gallery_photo.owlCarousel({

    merge: true,

    smartSpeed: 1000,

    loop: true,

    nav: false,

    autoplay: false,

    autoplayTimeout: 2000,

    responsiveClass: true,

    responsive: {

        0: {

            items: 1

        },

        600: {

            items: 3

        },

        1000: {

            items: 4

        }

    }

});

$('.gallery_nav_1 .testi_next').on('click', function () {

    gallery_photo.trigger('next.owl.carousel');

});

$('.gallery_nav_1 .testi_prev').on('click', function () {

    gallery_photo.trigger('prev.owl.carousel');

});


var gallery_photo_2 = $('.gallery_photo_2');

gallery_photo_2.owlCarousel({

    merge: true,

    smartSpeed: 1000,

    loop: true,

    nav: false,

    autoplay: false,

    autoplayTimeout: 2000,

    responsiveClass: true,

    responsive: {

        0: {

            items: 1

        },

        600: {

            items: 3

        },

        1000: {

            items: 4

        }

    }

});

$('.gallery_nav_2 .testi_next').on('click', function () {

    gallery_photo_2.trigger('next.owl.carousel');

});

$('.gallery_nav_2 .testi_prev').on('click', function () {

    gallery_photo_2.trigger('prev.owl.carousel');

});


/*---------------------------
career cards
------------------------------ */


var career_cards = $('.all_blogs');

career_cards.owlCarousel({

    merge: true,

    smartSpeed: 1000,

    loop: true,

    nav: false,

    autoplay: false,

    autoplayTimeout: 2000,

    responsiveClass: true,

    responsive: {

        0: {

            items: 1

        },

        600: {

            items: 3

        },

        1000: {

            items: 3

        }

    }

});


$('.career_nav .testi_next').on('click', function () {

    career_cards.trigger('next.owl.carousel');

});

$('.career_nav .testi_prev').on('click', function () {

    career_cards.trigger('prev.owl.carousel');

});

/*----------------------
Sub-services
------------------------- */

var cards = $('.all_subservices');

cards.owlCarousel({

    merge: true,

    smartSpeed: 1000,

    margin: 5,

    loop: true,

    nav: false,

    autoplay: false,

    autoplayTimeout: 2000,

    responsiveClass: true,

    responsive: {

        0: {

            items: 1

        },

        600: {

            items: 3

        },

        1000: {

            items: 3

        }

    }

});

$('.career_nav .testi_next').on('click', function () {

    cards.trigger('next.owl.carousel');

});
$('.career_nav .testi_prev').on('click', function () {
    cards.trigger('prev.owl.carousel');
});

/*----------------------

Career (detail.html

----------------------- */

$(".has-sub:not(:first)").attr('class', ' ');
$(".email-class").hide();
$("label[for='email_title']").hide();

$("#cards-heading").click(function () {
    var offset = 20; //Offset of 20px

    $('html, body').animate({
        scrollTop: $("#vacancy").offset().top - offset
    }, 800);
});

$("#goto-cards").click(function () {
    var offset = 100; //Offset of 100px

    $('html, body').animate({
        scrollTop: $("#interesting-heading").offset().top - offset
    }, 400);
});

$("#goto-vacancy").click(function () {
    var offset = 100; //Offset of 20px

    $('html, body').animate({
        scrollTop: $("#vacancy").offset().top - offset
    }, 1000);
});
$("#goto-map").click(function () {
    var offset = 100; //Offset of 20px

    $('html, body').animate({
        scrollTop: $("#map").offset().top - offset
    }, 1000);
});

$(".card-collapse").hide()

function collapfunc(detail_id) {
    var offset = 100; //Offset of 100px
    console.log("hello clikced")
    $(".card-collapse").hide()
    $(detail_id).show()
    $('html, body').animate({
        scrollTop: $(detail_id).offset().top - offset
    }, 800);
}

function collaphide() {
    var offset = 100; //Offset of 100px
    $(".card-collapse").hide()
    $('html, body').animate({
        scrollTop: $("#interesting-heading").offset().top - offset
    }, 800);
}


/*---------------------------

Notice detail.html

----------------------------- */

var lst = document.getElementsByClassName("btn-sm")
for (i = 0; i < lst.length; i++) {
    lst[i].style.display = "none";
}


/*-------------------------------

archive_month

--------------------------------- */

window.fbAsyncInit = function () {
    FB.init({
        appId: '95100348886',
        xfbml: true,
        version: 'v2.6'
    });
};

(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {
        return;
    }
    js = d.createElement(s);
    js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

/*------------------------

contact

-------------------------- */

function validation_error(event) {
    var email = document.getElementById("email_field");
    var name = document.getElementById("id_name");
    var company_name = document.getElementById("id_company_name");
    var contact_num = document.getElementById("id_contact_num");

    if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email.value))) {
        email.style.backgroundColor = "yellow";
        event.preventDefault();
    }
    if (!(/^[A-Za-z\s]+$/.test(name.value))) {
        name.style.backgroundColor = "yellow";
        event.preventDefault();
    }
    if (!(/^[A-Za-z\s]+$/.test(company_name.value))) {
        company_name.style.backgroundColor = "yellow";
        event.preventDefault();
    }
    if (!(/^(\+\d{1,3}[- ]?)?\d{10}$/.test(contact_num.value))) {
        contact_num.style.backgroundColor = "yellow";
        event.preventDefault();
    }
}


//Training and notice
function notice_validation(event) {
    var email = document.getElementById("email_field");
    var name = document.getElementById("id_name");
    var phone = document.getElementById("phone");

    if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email.value))) {
        email.style.backgroundColor = "yellow";
        event.preventDefault();
    }

    if (!(/^[A-Za-z\s]+$/.test(name.value))) {
        name.style.backgroundColor = "yellow";
        event.preventDefault();
    }

    if (!(/^(\+\d{1,3}[- ]?)?\d{10}$/.test(phone.value))) {
        phone.style.backgroundColor = "yellow";
        event.preventDefault();
    }

}

function collapshow(detail_id) {
    if ($(".event-collapse" + detail_id).is(":visible")) {
        $(".collapse").hide()
    }
    else {
        $(".collapse").hide()
        $(".event-collapse" + detail_id).show()
    }
}

/*----------------------

Training Page

-------------------------- */

$(document).ready(function () {
    $(".expand ").removeAttr('style');
});

$("#viewbtn").click(function () {
    $.ajax({
        method: 'GET',
        url: "{% url 'calendar' %}",
        dataType: 'json',
        success: function (data) {
            $('#calendar').fullCalendar({
                header: {
                    left: 'title',
                    center: '',
                    right: 'today prev,next'
                },
                height: 700,
                width: 900,
                themeSystem: 'bootstrap3',
                weekNumbers: false,
                eventLimit: false, // allow "more" link when too many events
                events: data,
                eventClick: function (data) {
                    window.location = "{% url 'traininghome'  slug='slug' %}".replace('slug', data.event_on__slug);
                }
            });

            $(".table-bordered").css("background", "silver");

        }
    });
});

 document.getElementsByClassName("expand")[0].removeAttribute("style");

    $(document).on("click", ".open-modal", function() {
        var title = $(this).data('heading');
        var content = $(this).data('content');
        $('.modal-title').html(title);
        $('.modal-body').html(content);

    });