/* Base */
body {
    line - height: 1.7;
    color: #cfcfd1;
    font - weight: 300;
    font - size: 1 rem;
    background: #232531;



    font-family: "Roboto Mono", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"; }



  



  ::selection {



    background: # 000;
    color: #fff;
}

a {
    -webkit - transition: .3 s all ease; -
    o - transition: .3 s all ease;
    transition: .3 s all ease;
}
a: hover {
    text - decoration: none;
}

h1, h2, h3, h4,
.h1, .h2, .h3, .h4 {
    font - family: "Roboto Mono", -apple - system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans - serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
}

.site - wrap: before {
    -webkit - transition: .3 s all ease - in -out; -
    o - transition: .3 s all ease - in -out;
    transition: .3 s all ease - in -out;
    background: rgba(0, 0, 0, 0.6);
    content: "";
    position: absolute;
    z - index: 2000;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    opacity: 0;
    visibility: hidden;
}

.offcanvas - menu.site - wrap {
        position: absolute;
        height: 100 % ;
        width: 100 % ;
        z - index: 2;
        overflow: hidden;
    }
    .offcanvas - menu.site - wrap: before {
        opacity: 1;
        visibility: visible;
    }

.btn {
    text - transform: uppercase;
    letter - spacing: .2e m;
    border - radius: 0;
}
.btn: hover, .btn: active, .btn: focus {
    outline: none; -
    webkit - box - shadow: none!important;
    box - shadow: none!important;
}

.form - control {
        height: 43 px;
        border - radius: 0;
    }
    .form - control: active, .form - control: focus {
        border - color: #ff5733;
    }
    .form - control: hover, .form - control: active, .form - control: focus {
        -webkit - box - shadow: none!important;
        box - shadow: none!important;
    }

.site - section {
    padding: 2.5e m 0;
}
@media(min - width: 768 px) {
    .site - section {
        padding: 10e m 0;
    }
}

.site - section - heading h2 {
    position: relative;
    font - size: 2.5 rem;
    color: #fff;
    padding - bottom: 30 px;
}
@media(min - width: 768 px) {
        .site - section - heading h2 {
            font - size: 3 rem;
        }
    }
    .site - section - heading h2: after {
        content: "";
        left: 0 % ;
        bottom: 0;
        position: absolute;
        width: 100 px;
        height: 2 px;
        background: -webkit - gradient(linear, left top, right top, from(#c70039), color - stop(70 % , #ff5733));
        background: -webkit - linear - gradient(left, #c70039, #ff5733 70 % );
        background: -o - linear - gradient(left, #c70039, #ff5733 70 % );
        background: linear - gradient(to right, #c70039, #ff5733 70 % );
    }
@media(min - width: 992 px) {
        .site - section - heading h2: after {
            left: -20 % ;
        }
    }
    .site - section - heading h2.text - center: after {
        content: ""; -
        webkit - transform: translateX(-50 % ); -
        ms - transform: translateX(-50 % );
        transform: translateX(-50 % );
        content: "";
        left: 50 % ;
        bottom: 0;
        position: absolute;
        width: 100 px;
        height: 2 px;
    }

.border - top {
    border - top: 1 px solid# edf0f5!important;
}

.site - footer {
        padding: 4e m 0;
        background: #1b1d24; }



    @media (min-width: 768px) {



      .site-footer {



        padding: 8em 0; } }



    .site-footer .border-top {



      border-top: 1px solid rgba(255, 255, 255, 0.1) !important; }



    .site-footer h2, .site-footer h3, .site-footer h4 {



      color: # fff;
    }
    .site - footer a {
        color: #fff;
    }
    .site - footer a: hover {
        color: #ff5733;
    }
    .site - footer ul li {
        margin - bottom: 10 px;
    }
    .site - footer.footer - heading {
        font - size: 16 px;
        color: #818186 !important; }



  



  .program h2 {



    font-size: 1.5rem; }



  



  .program .border-top {



    border-top: 1px solid # 383 b4f!important;
    }

.program.border - bottom {
    border - bottom: 1 px solid #383b4f !important; }



  



  .blog-entry h2 {



    font-size: 20px; }



    .blog-entry h2 a {



      color: # fff;
}

.blog - entry.post - meta {
        font - size: 14 px;
    }
    .blog - entry.post - meta a {
        color: #ff5733;
    }
    .blog - entry.post - meta img {
        width: 36 px;
        border - radius: 50 % ;
    }

/* Navbar */
.site - navbar {
        margin - bottom: 0 px;
        z - index: 1999;
        position: absolute;
        width: 100 % ;
    }
    .site - navbar.transparent {
        background: transparent;
    }
    .site - navbar.absolute {
        position: absolute;
        top: 0;
        left: 0;
        width: 100 % ;
    }
    .site - navbar.site - navigation.border - bottom {
        border - bottom: 1 px solid# f3f3f4!important;
    }
    .site - navbar.site - navigation.site - menu {
        margin - bottom: 0;
    }
    .site - navbar.site - navigation.site - menu.active > a {
        color: #ff5733;
        position: relative;
    }
    .site - navbar.site - navigation.site - menu.active > a: after {
        content: "";
        background: -webkit - gradient(linear, left top, right top, from(#c70039), color - stop(70 % , #ff5733));
        background: -webkit - linear - gradient(left, #c70039, #ff5733 70 % );
        background: -o - linear - gradient(left, #c70039, #ff5733 70 % );
        background: linear - gradient(to right, #c70039, #ff5733 70 % );
        width: 100 % ;
        height: 2 px;
        position: absolute;
        left: 0;
        bottom: 0;
    }
    .site - navbar.site - navigation.site - menu a {
        text - decoration: none!important;
        display: inline - block;
        text - transform: uppercase;
        letter - spacing: .1e m;
        font - size: 14 px;
    }
    .site - navbar.site - navigation.site - menu > li {
        display: inline - block;
        padding: 10 px 10 px;
    }
    .site - navbar.site - navigation.site - menu > li > a {
        padding: 10 px 0 px;
        color: #fff;
        text - decoration: none!important;
        position: relative;
    }
    .site - navbar.site - navigation.site - menu > li > a: after {
        content: "";
        background: -webkit - gradient(linear, left top, right top, from(#c70039), color - stop(70 % , #ff5733));
        background: -webkit - linear - gradient(left, #c70039, #ff5733 70 % );
        background: -o - linear - gradient(left, #c70039, #ff5733 70 % );
        background: linear - gradient(to right, #c70039, #ff5733 70 % );
        width: 0;
        height: 2 px;
        position: absolute;
        left: 0;
        bottom: 0; -
        webkit - transition: .3 s all ease - in -out; -
        o - transition: .3 s all ease - in -out;
        transition: .3 s all ease - in -out;
    }
    .site - navbar.site - navigation.site - menu > li > a: hover {
        color: #ff5733;
    }
    .site - navbar.site - navigation.site - menu > li > a: hover: after {
        width: 100 % ;
    }
    .site - navbar.site - navigation.site - menu > li.cta > a {
        border: 2 px solid #3f4046;



          padding-left: 20px;



          padding-right: 20px;



          color: # ff5733;
    }
    .site - navbar.site - navigation.site - menu > li.cta > a: hover {
        color: #fff;
    }
    .site - navbar.site - navigation.site - menu > li.cta > a: hover: after {
        display: none;
    }
    .site - navbar.site - navigation.site - menu.has - children {
        position: relative;
    }
    .site - navbar.site - navigation.site - menu.has - children > a {
        position: relative;
        padding - right: 20 px;
    }
    .site - navbar.site - navigation.site - menu.has - children > a: before {
        position: absolute;
        content: "\e313";
        font - size: 16 px;
        top: 50 % ;
        right: 0; -
        webkit - transform: translateY(-50 % ); -
        ms - transform: translateY(-50 % );
        transform: translateY(-50 % );
        font - family: 'icomoon';
    }
    .site - navbar.site - navigation.site - menu.has - children.dropdown {
        visibility: hidden;
        opacity: 0;
        top: 100 % ;
        position: absolute;
        text - align: left;
        border - top: 2 px solid# ff5733; -
        webkit - box - shadow: 0 2 px 10 px - 2 px rgba(0, 0, 0, 0.1);
        box - shadow: 0 2 px 10 px - 2 px rgba(0, 0, 0, 0.1);
        border - left: 1 px solid# edf0f5;
        border - right: 1 px solid# edf0f5;
        border - bottom: 1 px solid# edf0f5;
        padding: 0 px 0;
        margin - top: 20 px;
        margin - left: 0 px;
        background: #fff; -
        webkit - transition: 0.2 s 0 s; -
        o - transition: 0.2 s 0 s;
        transition: 0.2 s 0 s;
    }
    .site - navbar.site - navigation.site - menu.has - children.dropdown a {
        text - transform: none;
        letter - spacing: normal; -
        webkit - transition: 0 s all; -
        o - transition: 0 s all;
        transition: 0 s all;
        color: #343a40; }



          .site-navbar .site-navigation .site-menu .has-children .dropdown .active > a {



            color: # ff5733!important;
    }
    .site - navbar.site - navigation.site - menu.has - children.dropdown > li {
        list - style: none;
        padding: 0;
        margin: 0;
        min - width: 200 px;
    }
    .site - navbar.site - navigation.site - menu.has - children.dropdown > li > a {
        padding: 9 px 20 px;
        display: block;
    }
    .site - navbar.site - navigation.site - menu.has - children.dropdown > li > a: hover {
        background: #f4f5f9;
        color: #25262a; }



            .site-navbar .site-navigation .site-menu .has-children .dropdown > li.has-children > a:before {



              content: "\e315";



              right: 20px; }



            .site-navbar .site-navigation .site-menu .has-children .dropdown > li.has-children > .dropdown, .site-navbar .site-navigation .site-menu .has-children .dropdown > li.has-children > ul {



              left: 100%;



              top: 0; }



            .site-navbar .site-navigation .site-menu .has-children .dropdown > li.has-children:hover > a, .site-navbar .site-navigation .site-menu .has-children .dropdown > li.has-children:active > a, .site-navbar .site-navigation .site-menu .has-children .dropdown > li.has-children:focus > a {



              background: # f4f5f9;
        color: #25262a; }



        .site-navbar .site-navigation .site-menu .has-children:hover > a, .site-navbar .site-navigation .site-menu .has-children:focus > a, .site-navbar .site-navigation .site-menu .has-children:active > a {



          color: # ff5733;
    }
    .site - navbar.site - navigation.site - menu.has - children: hover, .site - navbar.site - navigation.site - menu.has - children: focus, .site - navbar.site - navigation.site - menu.has - children: active {
        cursor: pointer;
    }
    .site - navbar.site - navigation.site - menu.has - children: hover > .dropdown, .site - navbar.site - navigation.site - menu.has - children: focus > .dropdown, .site - navbar.site - navigation.site - menu.has - children: active > .dropdown {
        -webkit - transition - delay: 0 s; -
        o - transition - delay: 0 s;
        transition - delay: 0 s;
        margin - top: 0 px;
        visibility: visible;
        opacity: 1;
    }

.site - mobile - menu {
        width: 300 px;
        position: fixed;
        right: 0;
        z - index: 2000;
        padding - top: 20 px;
        background: #fff;
        height: calc(100 vh); -
        webkit - transform: translateX(110 % ); -
        ms - transform: translateX(110 % );
        transform: translateX(110 % ); -
        webkit - box - shadow: -10 px 0 20 px - 10 px rgba(0, 0, 0, 0.1);
        box - shadow: -10 px 0 20 px - 10 px rgba(0, 0, 0, 0.1); -
        webkit - transition: .3 s all ease - in -out; -
        o - transition: .3 s all ease - in -out;
        transition: .3 s all ease - in -out;
    }
    .offcanvas - menu.site - mobile - menu {
        -webkit - transform: translateX(0 % ); -
        ms - transform: translateX(0 % );
        transform: translateX(0 % );
    }
    .site - mobile - menu.site - mobile - menu - header {
        width: 100 % ;
        float: left;
        padding - left: 20 px;
        padding - right: 20 px;
    }
    .site - mobile - menu.site - mobile - menu - header.site - mobile - menu - close {
        float: right;
        margin - top: 8 px;
    }
    .site - mobile - menu.site - mobile - menu - header.site - mobile - menu - close span {
        font - size: 30 px;
        display: inline - block;
        padding - left: 10 px;
        padding - right: 0 px;
        line - height: 1;
        cursor: pointer; -
        webkit - transition: .3 s all ease; -
        o - transition: .3 s all ease;
        transition: .3 s all ease;
    }
    .site - mobile - menu.site - mobile - menu - header.site - mobile - menu - close span: hover {
        color: #25262a; }



    .site-mobile-menu .site-mobile-menu-body {



      overflow-y: scroll;



      -webkit-overflow-scrolling: touch;



      position: relative;



      padding: 0 20px 20px 20px;



      height: calc(100vh - 52px);



      padding-bottom: 150px; }



    .site-mobile-menu .site-nav-wrap {



      padding: 0;



      margin: 0;



      list-style: none;



      position: relative; }



      .site-mobile-menu .site-nav-wrap a {



        padding: 10px 20px;



        display: block;



        position: relative;



        color: # 212529;
    }
    .site - mobile - menu.site - nav - wrap a: hover {
        color: #ff5733;
    }
    .site - mobile - menu.site - nav - wrap li {
        position: relative;
        display: block;
    }
    .site - mobile - menu.site - nav - wrap li.active > a {
        color: #ff5733;
    }
    .site - mobile - menu.site - nav - wrap.arrow - collapse {
        position: absolute;
        right: 0 px;
        top: 10 px;
        z - index: 20;
        width: 36 px;
        height: 36 px;
        text - align: center;
        cursor: pointer;
        border - radius: 50 % ;
    }
    .site - mobile - menu.site - nav - wrap.arrow - collapse: hover {
        background: #f8f9fa;
    }
    .site - mobile - menu.site - nav - wrap.arrow - collapse: before {
        font - size: 12 px;
        z - index: 20;
        font - family: "icomoon";
        content: "\f078";
        position: absolute;
        top: 50 % ;
        left: 50 % ; -
        webkit - transform: translate(-50 % , -50 % ) rotate(-180 deg); -
        ms - transform: translate(-50 % , -50 % ) rotate(-180 deg);
        transform: translate(-50 % , -50 % ) rotate(-180 deg); -
        webkit - transition: .3 s all ease; -
        o - transition: .3 s all ease;
        transition: .3 s all ease;
    }
    .site - mobile - menu.site - nav - wrap.arrow - collapse.collapsed: before {
        -webkit - transform: translate(-50 % , -50 % ); -
        ms - transform: translate(-50 % , -50 % );
        transform: translate(-50 % , -50 % );
    }
    .site - mobile - menu.site - nav - wrap > li {
        display: block;
        position: relative;
        float: left;
        width: 100 % ;
    }
    .site - mobile - menu.site - nav - wrap > li > a {
        padding - left: 20 px;
        font - size: 20 px;
    }
    .site - mobile - menu.site - nav - wrap > li > ul {
        padding: 0;
        margin: 0;
        list - style: none;
    }
    .site - mobile - menu.site - nav - wrap > li > ul > li {
        display: block;
    }
    .site - mobile - menu.site - nav - wrap > li > ul > li > a {
        padding - left: 40 px;
        font - size: 16 px;
    }
    .site - mobile - menu.site - nav - wrap > li > ul > li > ul {
        padding: 0;
        margin: 0;
    }
    .site - mobile - menu.site - nav - wrap > li > ul > li > ul > li {
        display: block;
    }
    .site - mobile - menu.site - nav - wrap > li > ul > li > ul > li > a {
        font - size: 16 px;
        padding - left: 60 px;
    }

/* Blocks */
.container - fluid {
    max - width: 1400 px;
}

.site - hero {
        margin - bottom: 10 rem;
    }
    .site - hero, .site - hero.row {
        min - height: 700 px;
        height: calc(100 vh - 95 px);
    }
    .site - hero.inner, .site - hero.inner.row {
        min - height: 400 px;
        height: calc(50 vh - 95 px);
    }
    .site - hero h1 {
        font - size: 2 rem;
        background: -webkit - gradient(linear, left top, right top, from(#c70039), color - stop(70 % , #ff5733));
        background: -webkit - linear - gradient(left, #c70039, #ff5733 70 % );
        background: -o - linear - gradient(left, #c70039, #ff5733 70 % );
        background: linear - gradient(to right, #c70039, #ff5733 70 % ); -
        webkit - background - clip: text; -
        webkit - text - fill - color: transparent;
    }
@media(min - width: 992 px) {
        .site - hero h1 {
            font - size: 6 rem;
        }
    }
    .site - hero.caption {
        color: #fff;
    }
@media(min - width: 768 px) {
    .site - hero.caption {
        font - size: 1.7 rem;
    }
}

.btn - custom {
text - transform: uppercase;
color: #fff!important;
background: #3f4046;



    padding: 16px 30px;



    display: inline-block;



    letter-spacing: .2em;



    position: relative; }



    .btn-custom > span {



      position: relative;



      z-index: 2; }



    .btn-custom:before {



      background: -webkit-gradient(linear, left top, right top, from(# c70039), color - stop(70 % , #ff5733));
background: -webkit - linear - gradient(left, #c70039, #ff5733 70 % );
background: -o - linear - gradient(left, #c70039, #ff5733 70 % );
background: linear - gradient(to right, #c70039, #ff5733 70 % );
content: "";
position: absolute;
left: 0;
bottom: 0;
top: 0;
width: 0; -
webkit - transition: .3 s all ease - in -out; -
o - transition: .3 s all ease - in -out;
transition: .3 s all ease - in -out;
z - index: 1;
}
.btn - custom: hover: before {
    width: 100 % ;
}

.coordinator img {
    max - width: 50 px;
    border - radius: 50 % ;
}

.speaker {
    margin - bottom: 50 px;
}
.speaker.name {
    left: -80 px;
    position: relative;
}
@media(max - width: 1199.98 px) {
    .speaker.name {
        left: 0;
    }
}

.testimony {
    max - width: 500 px;
}
.testimony figure {
    margin - bottom: 40 px;
    text - align: center;
}
.testimony figure img {
    margin: 0 auto;
    max - width: 150 px;
    border - radius: 50 % ;
}
.testimony.author {
        margin - top: 50 px;
        color: #fff;
    }
    .testimony.text - muted {
        color: #e9e9ea;
    }

.form - group.form - control {
        color: #fff!important;
        background: none;
        border: 2 px solid# fff;
    }
    .form - group.form - control: active, .form - group.form - control: focus {
        background: none;
    }

.pricing {
    border: 2 px solid# ff5733;
    padding: 30 px;
}
.pricing h2 {
    font - size: 26 px;
    color: #fff;
    margin - bottom: 30 px;
}
.pricing.amount {
        color: #ff5733;
        margin - bottom: 30 px;
    }
    .pricing.amount sup {
        top: -30 px;
        font - size: 18 px;
    }
    .pricing.amount.number {
        font - size: 3 rem;
    }
    .pricing ul li {
        margin - bottom: 10 px;
    }

.slide - one - item {
        position: relative;
        z - index: 1;
    }
    .slide - one - item.owl - nav {
        position: relative;
        position: absolute;
        bottom: -90 px;
        left: 50 % ; -
        webkit - transform: translateX(-50 % ); -
        ms - transform: translateX(-50 % );
        transform: translateX(-50 % );
    }
    .slide - one - item.owl - nav.owl - prev, .slide - one - item.owl - nav.owl - next {
        position: relative;
        display: inline - block;
        padding: 20 px;
        font - size: 30 px;
        color: #000; }



         .slide-one-item .owl-nav .owl-prev.disabled, .slide-one-item .owl-nav .owl-next.disabled {



          opacity: .2; }



  



  .slide-one-item.home-slider .owl-nav {



    position: absolute !important;



    top: 50% !important;



    bottom: auto !important;



    width: 100%; }



  



  .slide-one-item.home-slider .owl-prev {



    left: 10px !important; }



  



  .slide-one-item.home-slider .owl-next {



    right: 10px !important; }



  



  .slide-one-item.home-slider .owl-prev, .slide-one-item.home-slider .owl-next {



    color: # fff;
        position: absolute!important;
        top: 50 % ;
        padding: 0 px;
        height: 50 px;
        width: 50 px;
        border - radius: 50 % ; -
        webkit - transform: translateY(-50 % ); -
        ms - transform: translateY(-50 % );
        transform: translateY(-50 % );
        background: rgba(0, 0, 0, 0.2); -
        webkit - transition: .3 s all ease - in -out; -
        o - transition: .3 s all ease - in -out;
        transition: .3 s all ease - in -out;
        line - height: 0;
        text - align: center;
        font - size: 25 px;
    }
@media(min - width: 768 px) {
        .slide - one - item.home - slider.owl - prev, .slide - one - item.home - slider.owl - next {
            font - size: 25 px;
        }
    }
    .slide - one - item.home - slider.owl - prev > span, .slide - one - item.home - slider.owl - next > span {
        position: absolute;
        line - height: 0;
        top: 50 % ;
        left: 50 % ; -
        webkit - transform: translate(-50 % , -50 % ); -
        ms - transform: translate(-50 % , -50 % );
        transform: translate(-50 % , -50 % );
    }
    .slide - one - item.home - slider.owl - prev: hover, .slide - one - item.home - slider.owl - prev: focus, .slide - one - item.home - slider.owl - next: hover, .slide - one - item.home - slider.owl - next: focus {
        background: black;
    }

.slide - one - item.home - slider: hover.owl - nav, .slide - one - item.home - slider: focus.owl - nav, .slide - one - item.home - slider: active.owl - nav {
    opacity: 10;
    visibility: visible;
}

.custom - pagination a, .custom - pagination span {
    display: inline - block;
    width: 40 px;
    height: 40 px;
    line - height: 40 px;
}