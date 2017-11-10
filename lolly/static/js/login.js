$('.login-input').on('focus', function() {
  $('.login').addClass('focused');
});

$('.login').on('submit', function(e) {
  e.preventDefault();
  $('.login').removeClass('focused').addClass('loading');
  $.ajax({
       url: "/login",
       type:"POST",
       data: {username:$('#username').val(),
              userpass:$('#userpass').val(),
              csrfmiddlewaretoken: csrf_token
              },
       success: function (data) {
         if (data == "success")
         {
           window.location.replace(window.location.pathname);
         }
         else{
           alert("Wrong");
           $('.login').addClass('focused').removeClass('loading');
         }
       }
     });
});
