$(document).ready(function(){
  console.log('START JS');
  init_datepicker();
  choose_table();
});

function init_datepicker(){
  $('#datepicker').datepicker({
    format: 'yyyy-mm-dd',
  }).on('changeDate', function(e,p){
    var date_str = String(e.date.getFullYear());
    if (e.date.getMonth() + 1 < 10){
      date_str = date_str + '-0' + String(e.date.getMonth() + 1);
    } else {
      date_str = date_str + '-' + String(e.date.getMonth() + 1);
    }
    if (e.date.getDate() < 10){
      date_str = date_str + '-0' + String(e.date.getDate());
    } else {
      date_str = date_str + '-' + String(e.date.getDate());
    }
    window.location = '/date/'+date_str;
  });
}

function choose_table(){
  $('.table').click(function(){
    if(!$(this).hasClass('reserved')){
        $(this).toggleClass('booked');
        update_tables();
    }
  });
}

function update_tables(){
  var booked_tables = $('.table.booked');
  $('input[name="tables"]').remove();
  if (booked_tables.length > 0){
    $('#booking').show();
    $.each(booked_tables, function(index, item){
      var iden = $(item).data('iden');
      $('#booking form').append('<input name="tables" type="hidden" value="'+iden+'">');
    });
  } else {
    $('#booking').hide();
  }
}
