$("#datepicker").datepicker("setDate", new Date());
$('#datepicker').datepicker({
    "setDate": new Date(),
    "autoclose": true
});

$("#typeSelector").change(function() {
  if ($(this).val() == "Expense") {
    $('#categorySelector').show();
  } else {
    $('#categorySelector').hide();
  }
});
$("#categorySelector").trigger("change");

$(document).ready(function(){
    $("#addEntryBtn").click(function(){
        $("#addEntryModal").modal();
    });
});