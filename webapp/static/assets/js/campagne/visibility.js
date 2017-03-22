
      function count_checked(list)
      {
        k=0;
        for (var i=0, max=list.length; i < max; i++) {
          if (list[i].id.substring(0, 9) == "checkbox_") 
              {
                if (list[i].checked)
                   {
                      k+=1;
                    }
              }
          }
        return k;  
      }

      function visibilite(thisId)
         {
            var thisCheck = document.getElementById(thisId);
            var Export_All_btn = document.getElementById("id_export_btn");
            var Delete_All_btn = document.getElementById("id_delete_btn");
            var all = document.getElementsByTagName("*");

        if ( thisId == "checkboxAll") {
              if (thisCheck.checked) {

                for (var i=0, max=all.length; i < max; i++) {
                   if (all[i].id.substring(0, 9) == "checkbox_") 
                      {
                        all[i].checked = true;
                       }
                   else if (all[i].id.substring(0, 9) == "recharge_") 
                      {
                        all[i].style.display = "none";
                      }
                   else if (all[i].id.substring(0, 5) == "bloc_") 
                      {
                       all[i].style.display = "none";
                      }
                  }
                k=count_checked(all);
                if(k==2){
                  Export_All_btn.style.display = "" ;
                  Delete_All_btn.style.display = "" ;
                } 
                else{
                  Export_All_btn.style.display = "" ;
                  Delete_All_btn.style.display = "" ;
                } 
                 
                }
              else {
                for (var i=0, max=all.length; i < max; i++) {
                   if (all[i].id.substring(0, 9) == "checkbox_")
                       {
                        all[i].checked = false;
                       }
                    else if (all[i].id.substring(0, 9) == "recharge_") 
                      {
                        all[i].style.display = "";
                      }
                   else if (all[i].id.substring(0, 5) == "bloc_") 
                      {
                       all[i].style.display = "";
                      }
                  }
                Export_All_btn.style.display = "none" ;
                Delete_All_btn.style.display = "none" ;
              }
            }
        else 
           {
                  document.getElementById("checkboxAll").checked=false;
                  k=count_checked(all);
                  if (k>2)
                            {
                               for (var i=0, max=all.length; i < max; i++) 
                                  {
                                     if (all[i].id.substring(0, 9) == "checkbox_") 
                                         {
                                             id_num = all[i].id.substring(9);
                                             document.getElementById("recharge_"+id_num).style.display = "none";
                                             document.getElementById("bloc_"+id_num).style.display = "none";  
                                          }
                                  }
                               Export_All_btn.style.display = "" ; 
                               Delete_All_btn.style.display = "" ;
                            }
                  else if (k==2) 
                            {
                               for (var i=0, max=all.length; i < max; i++) 
                                  {
                                     if (all[i].id.substring(0, 9) == "checkbox_") 
                                         {
                                             id_num = all[i].id.substring(9);
                                             document.getElementById("recharge_"+id_num).style.display = "none";
                                             document.getElementById("bloc_"+id_num).style.display = "none";  
                                          }
                                  }
                               Export_All_btn.style.display = "" ; 
                               Delete_All_btn.style.display = "" ;
                            }
                  else 
                           {  
                             if (thisCheck.checked)
                                  {
                                   for (var i=0, max=all.length; i < max; i++) 
                                      {
                                         if (all[i].id.substring(0, 9) == "checkbox_") 
                                             {  
                                                 id_num = all[i].id.substring(9);
                                                 document.getElementById("recharge_"+id_num).style.display = "none";
                                                 document.getElementById("bloc_"+id_num).style.display = "none"; 
                                              }
                                      }
                                    id_num = thisId.substring(9);
                                    document.getElementById("recharge_"+id_num).style.display = "";
                                    document.getElementById("bloc_"+id_num).style.display = ""; 

                                  }

                              else 
                                  {
                                   for (var i=0, max=all.length; i < max; i++) 
                                      {
                                         if (all[i].id.substring(0, 9) == "checkbox_") 
                                             {  
                                               id_num = all[i].id.substring(9);
                                               if  (k==1)
                                                  {
                                                    if (all[i].checked)
                                                      {
                                                        document.getElementById("recharge_"+id_num).style.display = "";
                                                         document.getElementById("bloc_"+id_num).style.display = "";  
                                                      }
                                                    else 
                                                      {
                                                         document.getElementById("recharge_"+id_num).style.display = "none";
                                                         document.getElementById("bloc_"+id_num).style.display = "none"; 
                                                      }
                                                  }
                                               else
                                                  {
                                                    document.getElementById("recharge_"+id_num).style.display = "";
                                                    document.getElementById("bloc_"+id_num).style.display = "";  
                                                  }  
                                                 

                                              }
                                      }
                                  }    

                              Export_All_btn.style.display = "none" ;
                              Delete_All_btn.style.display = "none" ;
                             }
                 }
       }
