$(document).on('change', '.is-last-round', function() {
  let parent = $(this).parent();
  let target = $(this).data('target');
  let show = $("option:selected", this).data('show');
  $(parent).find(target).children().addClass('hide');
  $(parent).find(show).removeClass('hide');
});

$(document).ready(function(){
    $('.is-last-round').trigger('change');
});