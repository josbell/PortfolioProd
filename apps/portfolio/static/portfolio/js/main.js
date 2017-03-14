
var main= function(){

	$('.dropdown img').click(function(){
		$('.dropdown-menu').toggle();
	});
	
	//Activate Carousel
	$("#myCarousel").carousel();
	
	//Enable Carousel Indicators
	$(".item1").click(function(){
		$("#myCarousel").carousel(0);
	});
	
	$(".item2").click(function(){
	$("#myCarousel").carousel(1);
	});
	
	//Enable Carousel Controls
	$(".left").click(function(){
		$("#myCarousel").carousel("prev");
	});
	
	$(".right").click(function(){
        $("#myCarousel").carousel("next");
	});
	

	$(".nav-pills li").click(function(){
		
		if(!$(this).hasClass('active')){ //if pill not already active
			var category = $(this).attr("class");
			//make all pills inactive
			$(".nav-pills li").removeClass('active');  
			
			//make this pill active
			$(this).addClass('active'); 

			//grab the class from li (javascript etc)
				
			
			if(category ==='all'){
				//make all imgs selected class
				$('.thumbnail img').addClass('selected');
				return false;
			}
			else{
				//remove selected class from all
				$('.thumbnail img').removeClass('selected');

				//add to imgs matching class
				$('.thumbnail img.'+ category).addClass('selected');

				return false;
			}
			
		};

		return false;

	});

/*
	$('.thumbnail img').click(function(){
		var modalBody = "";

		if($(this).hasClass('project1')){
			modalBody = "Review Books and check out other reviews";
		}
		else if($(this).hasClass('project2')){
			modalBody = "Description for Project2";
		}
		else if($(this).hasClass('project3')){
			modalBody = "Description for Project3";
		}

		$('.modal-body p').text(modalBody);
		$('#myModal').modal();

	});
*/

	$('a .project1').on('click', function(event){
		$('#project1Modal').modal();
	})

	$('a .project2').on('click', function(event){
		$('#project2Modal').modal();
	})

	$('a .project3').on('click', function(event){
		$('#project3Modal').modal();
	})

	$('a .project4').on('click', function(event){
		$('#project4Modal').modal();
	})

/*
  $('a').on('click',function(event){

    //Make sure this.has has a value before overriding default behavior
    if(this.hash !==""){
      //Prevent default anchor click behavior
      event.preventDefault();

      //Store hash
      var hash = this.hash;

      //Using jquery's animate() method to add smooth page scroll
      //The optimal number (800) specifies the number of milliseconds it takes to scroll to the specified area
          $('html, body').animate({
            scrollTop: $(hash).offset().top
          }, 800, function(){

          //Add hash (#) to URL when done scrolling (default click behavior)
          window.location.hash=hash;
        });
    }

    

  }); */


};

$(document).ready(main);

