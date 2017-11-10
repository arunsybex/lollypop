function groupAdd(){
  alert("arun")
  var values = [];
  $('.form-group input').each(function() {
      values.push($(this).val());
  });

  $.ajax({
    url: "/billAdd",
    method: "POST",
    data : {
      csrfmiddlewaretoken: csrf_token,
      gname : values[0],
      gvalue : values[1],
      gperiod : values[2],
      gbonus : values[3]
    },
    success:function(response){

        alert("success");
        //show_group();
  },
  error:function (xhr, textStatus, thrownError){
      alert("xhr status: " + xhr.statusText);
  }
  });
}

function show_group()
{
  $.ajax({
    url: "/groupShow",
    method: "POST",
    data : {
      csrfmiddlewaretoken: csrf_token,
    },
    success:function(response){

        $("#group_list").html(response)
  },
  error:function (xhr, textStatus, thrownError){
      alert("xhr status: " + xhr.statusText);
  }
  });
}

function group_update(e) {
  document.getElementById(e.id).setAttribute("data-toggle", "modal");
  document.getElementById(e.id).setAttribute("data-target", "#myModal");
  $.ajax({
    url: "/groupEdit",
    method: "GET",
    data : {
      csrfmiddlewaretoken: csrf_token,
      gid : e.id
    },
    success:function(response){
      $('#editpage').html(response)
  },
  error:function (xhr, textStatus, thrownError){
      alert("xhr status: " + xhr.statusText);
  }
  });
}

function groupUpdate() {
  var Evalues = [];
  $('.modal-body input').each(function() {
      Evalues.push($(this).val());
  });
    $.ajax({
      url: "/groupEdit",
      method: "POST",
      data : {
        csrfmiddlewaretoken: csrf_token,
        gid : Evalues[0],
        gname : Evalues[1],
        gvalue : Evalues[2],
        gperiod : Evalues[3],
        gbonus : Evalues[4]
      },
      success:function(response){
        alert(response);
        show_group();
    },
    error:function (xhr, textStatus, thrownError){
        alert("xhr status: " + xhr.statusText);
    }
    });
}

function group_delete(e) {
  $.ajax({
    url: "/groupDelete",
    method: "POST",
    data : {
      csrfmiddlewaretoken: csrf_token,
      gid : e.id
    },
    success:function(response){
      alert(response)
      show_group();
  },
  error:function (xhr, textStatus, thrownError){
      alert("xhr status: " + xhr.statusText);
  }
  });
}
