//This javascript has 2 function.
//Both are toggle and if else function. It's purpose is to either add classes or remove classes depending on the state when button is pressed.
//It will remove class that hides an element from screen and adds element that moves it to visiple part of the screen.

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
  }

//This is the second function.
//All functions are same but for mobile version.

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
