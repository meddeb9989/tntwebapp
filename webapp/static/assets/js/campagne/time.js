     var end_value = document.getElementById("end_value");
     var monthNames = [ "Jan", "Fev", "Mar", "Avr", "Mai", "Jui", "Jul", "Aou", "Sep", "Oct", "Nov", "Dec" ];   
     var today = new Date();
     var year = today.getFullYear();
     var month = monthNames[today.getMonth()];
     var day = today.getDate(); 
     var hours = today.getHours();
     var minutes = today.getMinutes();
     var now = day+" "+month+" "+year+" - "+hours+":"+minutes;
     var date_begin = document.getElementById("begin_date").value;
     var months = [];  
     months["Jan"] = "1";
     months["Fev"] = "2";
     months["Mar"] = "3";
     months["Avr"] = "4";
     months["Mai"] = "5";
     months["Jui"] = "6";
     months["Jul"] = "7";
     months["Aou"] = "8";
     months["Sep"] = "9";
     months["Oct"] = "10";
     months["Nov"] = "11";
     months["Dec"] = "12";

     if (date_begin.substring(0, 1) == "" )
        { 
          date_end_begin=now;
        }
      else 
        {
          var begin = date_begin.split(" ");
          var date = new Date(parseInt(begin[2]), parseInt(months[begin[1]])-1, parseInt(begin[0]), parseInt(begin[4].split(":")[0]), parseInt(begin[4].split(":")[1]));
          year = date.getFullYear();
          month = monthNames[date.getMonth()];
          day = date.getDate(); 
          hours = date.getHours();
          minutes = date.getMinutes();
          date_end_begin = day+" "+month+" "+year+" - "+hours+":"+minutes; 
        }

    $('.form_datetime_begin').datetimepicker({

        language:  'fr',
        weekStart: 1,
        todayBtn:  1,
        autoclose: 1,
        todayHighlight: 1,
        startView: 2,
        keyboardNavigation: 0,
        forceParse: 0,
        forceParse: false,
        startDate: now

    }).on('changeDate', function(ev) {
    var date_begin = $('.form_datetime_begin').data("datetimepicker").getDate();
    var date_end = $('.form_datetime_end').data("datetimepicker").getDate();
    document.getElementById("end_date_id").style.display = "";
    
    if ((date_begin.getHours()==23)&&(date_begin.getMinutes()==55))
      {
        date_begin.setDate(date_begin.getDate()+1);
      }

    year = date_begin.getFullYear();
    month = monthNames[date_begin.getMonth()];
    day = date_begin.getDate(); 
    hours = date_begin.getHours();
    minutes = date_begin.getMinutes()+5;
    var after = day+" "+month+" "+year+" - "+hours+":"+minutes;

    if (date_end.valueOf() != today.valueOf()){
       if (date_begin.valueOf() > date_end.valueOf()) {
                $('.form_datetime_end').datetimepicker('setStartDate', after);
                $('.form_datetime_end').datetimepicker('update').children("input").val("");
            }
    }
    else {   
            $('.form_datetime_end').datetimepicker('setStartDate', after);
            }
    
        });

    $('.form_datetime_end').datetimepicker({
        language:  'fr',
        weekStart: 1,
        todayBtn:  1,
        autoclose: 1,
        todayHighlight: 1,
        startView: 2,
        forceParse: false,
        startDate: date_end_begin
     });
