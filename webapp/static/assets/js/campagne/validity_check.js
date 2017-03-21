     var all = document.querySelectorAll('[id^="Date_"]');
     var monthNames = [ "Jan", "Fev", "Mar", "Avr", "Mai", "Jui", "Jul", "Aou", "Sep", "Oct", "Nov", "Dec" ];
     var begin;
     var end;
     var validity;
     var color;
     var campain_name;
     var date_begin;
     var date_end;
     var date_now = new Date();
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

     for (var i=0, max=all.length; i < max; i++) 
       {
               validity = document.getElementById("validity_"+all[i].id.substring(5));
               campain_name = document.getElementById("campain_name_"+all[i].id.substring(5));
               color = document.getElementById("color_"+all[i].id.substring(5));


               begin = document.getElementById("Date_"+all[i].id.substring(5)).value.split(" ");

               date_begin = new Date(parseInt(begin[2]), parseInt(months[begin[1]])-1, parseInt(begin[0]), parseInt(begin[4].split(":")[0]), parseInt(begin[4].split(":")[1]));
               
               var usertype = document.querySelector('[id^="usertype_"]');

               var timeDiff = Math.abs(date_now.getTime() - date_begin.getTime());
               var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24)); 

               if ((diffDays > 1) && (date_begin.valueOf() > date_now.valueOf()))
               	  {
                    
                    if (usertype.id=="usertype_Employeur")
                    {
                      validity.color = "green";
                      color.className="success";
                      validity.innerHTML = "Carte Valide";
                    }
                    else
                    {
                      validity.color = "orange";
                      color.className="warning";
                      validity.innerHTML = "Transaction En Cours...";
                      
                    }
                    
               	  }
               else if ((diffDays > 1) && (date_begin.valueOf() < date_now.valueOf()))
                 {
                    
                    if (usertype.id=="usertype_Employeur")
                    {
                      validity.color = "red";
                      color.className="danger";
                      validity.innerHTML = "Carte Expirée";
                    }
                    else
                    {
                      validity.color = "green";
                      color.className="success";
                      validity.innerHTML = "Transaction Effectuée";
                    }
                  }
                else 
                 {
                    
                    if (usertype.id=="usertype_Employeur")
                    {
                      validity.color = "orange";
                      color.className="warning";
                      validity.innerHTML = "Expire Bientot...";
                    }
                    else
                    {
                      validity.color = "orange";
                      campain_name.color = "white";
                      color.className="warning";
                      validity.innerHTML = "Transaction En Cours...";
                    }
                  }
	  
        }

