  function toggle1() {

  if ($("div.anchor11").hasClass("sidenav_show")) {
    hide1();
  } 
  else {
    show1();
  }
  }

  function hide1() {

  $("div.anchor11").addClass("sidenav_hide");
  $("div.anchor11").removeClass("sidenav_show");

  $("div.anchor13").addClass("content_full");
  $("div.anchor13").removeClass("content_minim");

  $("div.anchor14").removeClass("button3_maxim");
  $("div.anchor14").addClass("button3_minim");

  $("footer.footer").removeClass("footer_minim");
  $("footer.footer").addClass("footer_maxim");

  $("div.anchor16").removeClass("sidetop_hide");
  $("div.anchor16").addClass("sidetop_show");

  $("button.arrow_left").removeClass("arrow_left_show");
  $("button.arrow_left").addClass("arrow_left_hide");
  }

  function show1() {

  $("div.anchor11").addClass("sidenav_show");
  $("div.anchor11").removeClass("sidenav_hide");

  $("div.anchor13").removeClass("content_full");
  $("div.anchor13").addClass("content_minim");

  $("div.anchor14").addClass("button3_maxim");
  $("div.anchor14").removeClass("button3_minim");

  $("footer.footer").addClass("footer_minim");
  $("footer.footer").removeClass("footer_maxim");

  $("div.anchor16").addClass("sidetop_hide");
  $("div.anchor16").removeClass("sidetop_show");

  $("button.arrow_left").removeClass("arrow_left_hide");
  $("button.arrow_left").addClass("arrow_left_show");
  }

  function toggle2() {

  if ($("ul.anchor16").hasClass("topnav_hide")) {
    show();
  } 
  else {
    hide();
  }
  }


  function show() {

  $("ul.anchor16").addClass("topnav_show");
  $("ul.anchor16").removeClass("topnav_hide");

  $("div.anchor13").removeClass("content_top");
  $("div.anchor13").addClass("content_low");
  }

  function hide() {

  $("ul.anchor16").addClass("topnav_hide");
  $("ul.anchor16").removeClass("topnav_show");

  $("div.anchor13").removeClass("content_low");
  $("div.anchor13").addClass("content_top");
  }

function toggle3() {

  if ($("html").hasClass("background_1")) {
    next();
  } 
  else {
    previous();
  }
  }

  function next() {

  $("html").addClass("background_2");
  $("html").removeClass("background_1");

  $("div.anchor17").addClass("text_hidden");
  $("div.anchor18").removeClass("text_hidden");
  }

  function previous() {

  $("html").addClass("background_1");
  $("html").removeClass("background_2");

  $("div.anchor18").addClass("text_hidden");
  $("div.anchor17").removeClass("text_hidden");
  }
  
