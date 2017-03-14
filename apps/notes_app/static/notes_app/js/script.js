
           	$('form').submit(function(e){
            	console.log("Made it this far")
            	e.preventDefault()

            	$.ajax({
            		url: "/notes_app/new/",
            		method: 'post',
            		data: $(this).serialize(),
            		success: function(serverResponse){
            			$('.notes').html(serverResponse)
            			console.log("Received this from server", serverResponse)
            		}
            	})
            	$('.noteForm').trigger('reset')
            })
