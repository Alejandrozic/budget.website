// NAVBAR Toggle
$(function () {
  'use strict'
  $('[data-toggle="offcanvas"]').on('click', function () {
    $('.offcanvas-collapse').toggleClass('open')
  })
})

/*
    Javascript for switching active nav item/link.
*/

$(function () {
  var curr = location.pathname;
  $('.nav-link').each(function(){
    var $this = $(this);
    if ($this.attr('href') == curr){
        $(this).addClass('active');
    } else{
        $(this).removeClass('active');
    }
  })
})

$(function () {
  var curr = location.pathname;
  $('.nav-item').each(function(){
    var $this = $(this);
    if ($this.attr('href') == curr){
        $(this).addClass('active');
    } else{
        $(this).removeClass('active');
    }
  })
})