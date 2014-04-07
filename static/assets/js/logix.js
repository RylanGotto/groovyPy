$user_searchterms = new Array();
$musicfile_array = new Array();
$(document).ready(function(){
    create_searcharray();
  var ws = $.websocket("ws://localhost:8888/ws", {
        events: {
                next_track: function(e) { 

                        $("#nowplaying").empty();
                            $div = document.getElementById("playlist");
                            $musicdiv = $div.children[0];
                            $path = $musicdiv.children[0].value;
                            $filename = $musicdiv.children[1].innerHTML;
                        $($musicdiv).remove();
                        $("#nowplaying").append($filename);
                        ws.send('song', $path);
                        $("#recently_played").prepend(
                            "<div class='localmus dragsearch'>" 
                            + "<input type='hidden' value='" 
                            + $path 
                            + "'/> <p>"
                            + $filename
                            + "</p>"
                            );     
                }
        }
    });

$('#search_box').change(function (){
    get_searchterm(this.value);
    this.value = '';
    search_filenames();
});

$('.localmus').click( function(){
  $("#nowplaying").empty();
  $path = $(this).children().val();
  $filename = $(this).text();
  $("#nowplaying").append($filename);
  ws.send('song', $path);
  $("#recently_played").prepend(
    "<div class='localmus dragsearch'>" 
    + "<input type='hidden' value='" 
    + $path 
    + "'/> <p>"
    + $filename
    + "</p>"
    );
});

$('#next').click ( function(){
    $("#nowplaying").empty();
    var value = $('#pause').val()
    if (value.indexOf('play') >= 0) {
        $('#pause').val('pause');
    }
    $div = document.getElementById("playlist");
        $musicdiv = $div.children[0];
        $path = $musicdiv.children[0].value;
        $filename = $musicdiv.children[1].innerHTML;
    $($musicdiv).remove();
    $("#nowplaying").append($filename);
    ws.send('song', $path);
    $("#recently_played").prepend(
        "<div class='localmus dragsearch'>" 
        + "<input type='hidden' value='" 
        + $path 
        + "'/> <p>"
        + $filename
        + "</p>"
        );
});

$('#test').click ( function(){
    test();
});


$('.dragsearch').draggable({
    cursor: 'pointer',
    connectWith: '.dropme',
    helper: 'clone',
    opacity: 0.5,
    zIndex: 10
});

$('.dropme').sortable({
    connectWith: '.dropme',
    cursor: 'pointer'
}).droppable({
    accept: '.dragsearch',
    activeClass: 'highlight',
    drop: function(event, ui) {
        var $li = $("<div class='localmus'>").html(ui.draggable.html());
        $li.appendTo(this);
    }
});

  $('#pause').toggle(function (){
    $(this).val("play");
    ws.send('pause', '');
  },
  function (){
     $(this).val("pause");
    ws.send('pause', '');
  });
 
  
var slider = $('#slider'),  
    tooltip = $('.tooltip');  

tooltip.hide();  

slider.slider({  
    range: "min",  
    min: 1,  
    value: 35,  

    start: function(event,ui) {  
      tooltip.fadeIn('fast');  
    },  

    slide: function(event, ui) {  

        var value = slider.slider('value'),  
            volume = $('.volume');  

        tooltip.css('left', value).text(ui.value);  

        if(value <= 5) {   
            volume.css('background-position', '0 0');  
            ws.send('volume', value);
        }   
        else if (value <= 25) {  
            volume.css('background-position', '0 -25px');  
            ws.send('volume', value);
        }   
        else if (value <= 75) {  
            volume.css('background-position', '0 -50px');  
            ws.send('volume', value);
        }   
        else {  
            volume.css('background-position', '0 -75px');  
            ws.send('volume', value);
        };  

    },  

    stop: function(event,ui) {  
      tooltip.fadeOut('fast');  
    },  
});  
});

function search_filenames(){
    $x = 0;
    $serch_divs = new Array('div0','div1','div2','div3','div4');
    $results = new Array();
    for($i=0;$i<$musicfile_array.length;$i++){


                    $musicfile_terms = $musicfile_array[$i]['filename'].toLowerCase().replace(/[^A-Za-z\s]+/g, ' ').split(" ");

                        for($j=0;$j<$user_searchterms.length;$j++){
                            for($k=0;$k<$musicfile_terms.length;$k++){

                                if($user_searchterms[$j].localeCompare($musicfile_terms[$k]) == 0){

                                    $mainDiv = document.getElementById($serch_divs[$x]);
                                    $mainDiv.children[0].value = $musicfile_array[$i]['path'];
                                    $mainDiv.children[1].innerHTML = $musicfile_array[$i]['filename'];
                                    $x++;
                                } 
                               
                            }
                        }
                    
         } 
}

function create_searcharray(){
    $( ".localmus" ).each(function( index ) {
        $path = $(this).children().val();
        $filename = $(this).text();
        $dict = { 'path': $path, 'filename':$filename};
    $musicfile_array.push( $dict );
});

}

function get_searchterm(user_terms){
    $user_searchterms = user_terms.toLowerCase().split(" ");     
}
