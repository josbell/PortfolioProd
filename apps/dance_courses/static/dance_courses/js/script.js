$(document).ready(function(){
    $("#loginLink").click(function(){
        if ($('#registerModal').hasClass('in')){
          $("#registerModal").modal('hide');
        }//end if
        $("#loginModal").modal();
    });

    $("#registerLink").click(function(){
        if ($('#loginModal').hasClass('in')){
          $("#loginModal").modal('hide');
        }//end if
        $("#registerModal").modal();
    });

  // Add smooth scrolling to all links in navbar + footer link
  $(".navbar a, footer a[href='#myPage']").on('click', function(event) {
    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (900) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 900, function(){
   
        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
  
  $(window).scroll(function() {
    $(".slideanim").each(function(){
      var pos = $(this).offset().top;

      var winTop = $(window).scrollTop();
        if (pos < winTop + 600) {
          $(this).addClass("slide");
        }
    });
  });

  //Ajax call

  $('#loginForm').submit(function(e){
    console.log('made it to loginForm event handler')
    e.preventDefault()

    $.ajax({
        url: '/dance_courses/loginUsers/',
        method: 'post',
        data: $(this).serialize(),
        success: function(serverResponse){
          window.location.replace('/dance_courses/showUserCourses');

        },
        error: function(jqxhr){
          if(jqxhr.status == 403){
            $('#loginErrorMsg').text(jqxhr.responseText);
          }
          else{
            console.log(jqxhr.statusCode().status);
            $('#loginErrorMsg').text('Our systems our down temporarily, please try again later');
          }
        }
    })
  })

  $('#signupForm').submit(function(e){
    console.log('made it to signupForm event handler')
    e.preventDefault()

    $.ajax({
        url: '/dance_courses/createusers/',
        method: 'post',
        data: $(this).serialize(),
        success: function(serverResponse){
          window.location.replace('/dance_courses/showUserCourses');

        },
        error: function(jqxhr){
          if(jqxhr.status == 403){
            $('#registerErrorMsg').text(jqxhr.responseText);
          }
          else{
            console.log(jqxhr.statusCode().status);
            $('#registerErrorMsg').text('Our systems our down temporarily, please try again later');
          }
        }
    })
  })


})

