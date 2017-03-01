$(".button-collapse").sideNav();

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        
        reader.onload = function (e) {
            $('.img-container').css('display', 'block');
            $('#image').attr('src', e.target.result);
            $('#upload-box').hide();
            $('.search').css('display', 'block');
            $('.redo').css('display', 'block');
            
        }
        
        reader.readAsDataURL(input.files[0]);
    }
}

$("#file-input").change(function(){
    readURL(this);
}); 

function submitData() {
  $('#form').css('display', 'none');
  $('#loader').css('display', 'block')
  console.log("here");
};