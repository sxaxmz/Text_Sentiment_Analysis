$(document).ready(function() {
    $("#textarea_count").on('keyup', function() {
      var words = 0;
  
      if ((this.value.match(/\S+/g)) != null) {
        words = this.value.match(/\S+/g).length;
      }
  
      if (words > 2000) {
        var trimmed = $(this).val().split(/\s+/, 2000).join(" "); // Split the string on first 10000 words and rejoin on spaces
        $(this).val(trimmed + " ");  // Add a space at the end to make sure more typing creates new words
      } else {
        $('#display_count').text(words);
        $('#word_left').text(2000-words);
      }
    });

    $("analyze").on('click', function() {
      alert('clicked!');
      var txt = document.getElementsById("textarea_count").value;
      console.log(txt);
      $.get('read.txt', function(data) {
        console.log(data)
      });
      document.getElementById("textarea_count").value = "Clicked JS";
    })

    $('clear').click(function() {
      $("textarea_count").value = "";
    })
  
  });
  