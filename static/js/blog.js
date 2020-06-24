$("#new-post-form").submit(function (e) {
  e.preventDefault();
  var actionUrl = e.currentTarget.action;
  var input_file = document.getElementById("post-image");
  file = input_file.files[0];
  var form = $("#new-post-form")[0];
  var data = new FormData(form);
  var mimeType = file.type;
  if (mimeType.indexOf("image") >= 0 && mimeType != undefined) {
    $.ajax({
      url: actionUrl,
      type: "post",
      data: data,
      enctype: "multipart/form-data",
      processData: false,
      contentType: false,
      success: function (data) {
        if (data.status) {
          $("new-post-form").trigger("reset");
          toastr.success(data.message);
          window.location.href = "/my-posts/";
        }
      },
      error: function (data) {
        toastr.error(data.responseJSON.message);
      },
    });
  } else {
    toastr.error("The file must be one of the following types: .png, .jpeg, .jpg.");
  }
});
