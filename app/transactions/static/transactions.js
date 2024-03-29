/*
    Transaction Type and Category Filtering
*/

$("#transactionTypeName").change(function() {
  if ($(this).val() == "Expense") {
    $('#categoryNameSelector').show();
  } else {
    $('#categoryNameSelector').hide();
  }
});
$("#categoryNameSelector").trigger("change");

/*
    JavaScript and AJAX for UPDATE
*/

$(document).ready(function () {
    $('.update-modal-opener').click(function () {
        $.ajax({
            type: "GET",
            url: '/transactions/'+$(this).data('id'),
            success: function(result) {
                localStorage.setItem('transactionsUpdateId',result['id']);
                $('#transactionName').val(result['name']);
                $('#amount').val(result['amount']);
                $('#categoryName').val(result['category']);
                $('#transactionTypeName').val(result['transaction_type']);
                $('#date').val(result['date']);
                $('#updateTransactionsModal').modal();
            },
            error: function(request, status, error) {
                alert(request.responseText);
            }
        });
    });
});

function UpdateTransaction(){
	$.ajax({
		url : '/transactions/' + localStorage.getItem('transactionsUpdateId') + '/update',
		type : 'POST',
		async: false,
		data: {
		    date: $('#date').val(),
		    transactionTypeName: $('#transactionTypeName').val(),
		    categoryName: $('#categoryName').val(),
		    transactionName: $('#transactionName').val(),
		    amount: $('#amount').val()
		}
	});
}

/*
    Datepicket Init
*/

$("#datepicker").datepicker("setDate", new Date());
$('#datepicker').datepicker({
    "setDate": new Date(),
    "autoclose": true
});

/*
    Functions for new Transaction
*/

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
