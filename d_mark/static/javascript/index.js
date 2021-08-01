$(document).ready(function() {
    $(window).scroll(function() {
        if (this.scrollY > 20) {
            $('.navigation-bar').addClass("sticky");
            $('.navigation-bar .mobile_menu').addClass("sticky");
            $('.navigation-bar .mobile_menu li a').addClass("sticky");
            $('.navigation-bar .max-width .menu li a').addClass("lol");
            $('.navigation-bar .item ').addClass("faiz")
        } else {
            $('.navigation-bar').removeClass("sticky");
            $('.navigation-bar .mobile_menu').removeClass("sticky");
            $('.navigation-bar .mobile_menu li a').removeClass("sticky");
            $('.navigation-bar .max-width .menu li a').removeClass("lol");
            $('.navigation-bar .item ').removeClass("faiz")
        }
        if (this.scrollY > 300) {
            $('.scroll-up-btn').addClass("show");
        } else {
            $('.scroll-up-btn').removeClass("show");
        }
    });

    $('.hum-burger').click(function() {
        $('.navigation-bar .mobile_menu').toggleClass("active")
        $('.hum-burger .item-1').toggleClass("active")
        $('.hum-burger .item-2').toggleClass("active")
        $('.hum-burger .item-3').toggleClass("active")
        $('.hum-burger .item-4').toggleClass("active")
    });
    const sc_btn = document.querySelector(".scroll-up-btn");
    sc_btn.addEventListener("click", function() {
        window.scrollTo(0, 0);
    })
    var typed = new Typed(".typing-1", {
        strings: ['Salesmen.', 'Medical Representative.'],
        typeSpeed: 50,
        backSpeed: 60,
        loop: true,
    });
});