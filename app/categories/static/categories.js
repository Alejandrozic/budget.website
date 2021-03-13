/*
    JavaScript and AJAX for DELETE
*/

$(document).ready(function () {
    $('.delete-modal-opener').click(function () {
        localStorage.setItem('categoryDeleteId',$(this).data('id'));
        $('#deleteCategoryModal').modal();
    });
});

function DeleteCategory(){
	$.ajax({
		url : '/categories/' + localStorage.getItem('categoryDeleteId') + '/delete',
		type : 'POST'
	});
}

/*
    JavaScript and AJAX for UPDATE
*/

$(document).ready(function () {
    $('.update-modal-opener').click(function () {
        $.ajax({
            type: "GET",
            url: '/categories/'+$(this).data('id'),
            success: function(result) {
                localStorage.setItem('categoryUpdateId',result['id']);
                $('#updatedCategoryName').val(result['name']);
                $('#updateCategoryModal').modal();
            },
            error: function(request, status, error) {
                alert(request.responseText);
            }
        });
    });
});

function UpdateCategory(){
	$.ajax({
		url : '/categories/' + localStorage.getItem('categoryUpdateId') + '/update',
		type : 'POST',
		async: false,
		data: {
		    updatedCategoryName: $('#updatedCategoryName').val()
		}
	});
}

/*
    JavaScript and AJAX for NEW
*/

$(document).ready(function () {
    $('.new-modal-opener').click(function () {
        $('#newCategoryModal').modal();
    });
});

function NewCategory(){
	$.ajax({
		url : '/categories/new',
		type : 'POST',
		async: false,
		data: {
		    newCategoryName: $('#newCategoryName').val()
		}
	});
}