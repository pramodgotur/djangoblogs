$("#new-post-form").submit(function (e) {
  e.preventDefault();
  var actionUrl = e.currentTarget.action;
  var input_file = document.getElementById("post-image");
  file = input_file.files[0];
  var form = $("#new-post-form")[0];
  var data = new FormData(form);
  var mimeType = file.type;
  if (mimeType.indexOf("image") >= 0 && mimeType != undefined) {
    post_data(actionUrl, data);
  } else {
    toastr.error("The file must be one of the following types: .png, .jpeg, .jpg.");
  }
});

$(document).on("click", ".delete-post", function (e) {
  var post_id = $(this).attr("id");
  var actionUrl = "/delete-post/" + post_id + "/";
  $.ajax({
    url: actionUrl,
    type: "DELETE",
    success: function (data) {
      toastr.success(data.message);
      $("#post-" + post_id).remove();
      let post_exists = data.data.post_exists;
      if (post_exists == false) {
        let html_str = `
        <h1 class="text-center">My Posts</h1>
          <div class="offset-md-3 col-md-6">
          <div class="card">
            <div class="card-body">
              <p class="card-text">
                You don't have any posts yet...
              </p>
              <a href="/add-post/" class="btn btn-primary">Add New Post</a>
            </div>
          </div>
        </div>
        `;
        $("#my-posts").html(html_str);
      }
    },
    error: function (data) {
      toastr.error(data.responseJSON.message);
    },
  });
});

function post_data(actionUrl, data) {
  $.ajax({
    url: actionUrl,
    type: "post",
    data: data,
    enctype: "multipart/form-data",
    processData: false,
    contentType: false,
    success: function (data) {
      if (data.status) {
        let post_id = data.data.post_id;
        toastr.success(data.message);
        window.location.href = "/blog-detail/" + post_id + "/";
      }
    },
    error: function (data) {
      toastr.error(data.responseJSON.message);
    },
  });
}

$("#edit-post-form").submit(function (e) {
  e.preventDefault();
  var actionUrl = e.currentTarget.action;
  var input_file = document.getElementById("post-image");

  file = input_file.files[0];
  console.log(file);
  var form = $("#edit-post-form")[0];
  var data = new FormData(form);
  if (file != undefined) {
    var mimeType = file.type;
    if (mimeType.indexOf("image") >= 0 && mimeType != undefined) {
      post_data(actionUrl, data);
    } else {
      toastr.error("The file must be one of the following types: .png, .jpeg, .jpg.");
    }
  } else {
    post_data(actionUrl, data);
  }
});
