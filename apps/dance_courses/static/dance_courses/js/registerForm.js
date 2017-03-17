$().ready(function(){
	$('#signupForm').validate({
		rules:{
			firstname:{
				required:true,
				minlength:2
			},
			lastname:{
				required:true,
				minlength:2
			},
			username:{
				required:true,
				minlength:3,
				email:true
			},
			password:{
				required:true,
				minlength:3
			},
			confirm_password:{
				required:true,
				minlength:3,
				equalTo: "#password"
			}
		},

		messages:{
			firstname : {
				required: "Please enter your first name",
				minlength: "Your firstname must consist of at least 2 characters"
			},

			lastname: {
				required: "Please enter your last name",
				minlength: "Your last name must consist of at least 2 characters"
			},
			username: {
				required: "Please enter your email",
				minlength: "Your username must consist of at least 3 characters",
				email: "Your email is incorrect"
			},
			password:{
				required: "Please provide a password",
				minlength: "Your password must be at least 3 characters long"
			},

			confirm_password:{
				required: "Please provide a password",
				minlength: "Your password must be at least 3 characters long",
				equalTo: "Please enter the same password as above"
			}

		}
	});
});