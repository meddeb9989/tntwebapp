
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
            var Compare_All_btn = document.getElementById("id_compare_btn");
            var Delete_All_btn = document.getElementById("id_delete_btn");
            var Show_Valid = document.getElementById("id_show_valid_check");
            var Show_inValid = document.getElementById("id_show_invalid_check");
            var all = document.getElementsByTagName("*");

        if ( thisId == "checkboxAll") {
              if (thisCheck.checked) {

                for (var i=0, max=all.length; i < max; i++) {
                   if (all[i].id.substring(0, 9) == "checkbox_") 
                      {
                        all[i].checked = true;
                       }
                   else if (all[i].id.substring(0, 7) == "export_") 
                      {
                        all[i].style.display = "none";
                      }
                   else if (all[i].id.substring(0, 7) == "delete_") 
                      {
                       all[i].style.display = "none";
                      }
                  }
                k=count_checked(all);
                if(k==2){
                  Export_All_btn.style.display = "" ;
                  Compare_All_btn.style.display = "none" ;
                  Delete_All_btn.style.display = "" ;
                  Show_Valid.style.display = "none" ;
                  Show_inValid.style.display = "none" ;
                } 
                else{
                  Export_All_btn.style.display = "" ;
                  Compare_All_btn.style.display = "none" ;
                  Delete_All_btn.style.display = "" ;
                  Show_Valid.style.display = "none" ;
                  Show_inValid.style.display = "none" ;
                } 
                 
                }
              else {
                for (var i=0, max=all.length; i < max; i++) {
                   if (all[i].id.substring(0, 9) == "checkbox_")
                       {
                        all[i].checked = false;
                       }
                    else if (all[i].id.substring(0, 7) == "export_") 
                      {
                        all[i].style.display = "";
                      }
                   else if (all[i].id.substring(0, 7) == "delete_") 
                      {
                       all[i].style.display = "";
                      }
                  }
                Export_All_btn.style.display = "none" ;
                Compare_All_btn.style.display = "none" ;
                Delete_All_btn.style.display = "none" ;
                Show_Valid.style.display = "" ;
                Show_inValid.style.display = "" ;
              }
            }
        else if ( thisId == "show_Valid")
              {
               document.getElementById("show_inValid").checked=false;
               document.getElementById("show_Coming").checked=false;
               document.getElementById("myForm").submit();
              }
        else if ( thisId == "show_inValid") 
              {
               document.getElementById("show_Valid").checked=false;
               document.getElementById("show_Coming").checked=false;
               document.getElementById("myForm").submit();
              }
        else if ( thisId == "show_Coming")
              {
               document.getElementById("show_Valid").checked=false;
               document.getElementById("show_inValid").checked=false;
               document.getElementById("myForm").submit();
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
                                             document.getElementById("export_"+id_num).style.display = "none";
                                             document.getElementById("delete_"+id_num).style.display = "none";  
                                          }
                                  }
                               Export_All_btn.style.display = "none" ; 
                               Compare_All_btn.style.display = "none" ;
                               Delete_All_btn.style.display = "" ;
                               Show_Valid.style.display = "none" ;
                               Show_inValid.style.display = "none" ;
                            }
                  else if (k==2) 
                            {
                               for (var i=0, max=all.length; i < max; i++) 
                                  {
                                     if (all[i].id.substring(0, 9) == "checkbox_") 
                                         {
                                             id_num = all[i].id.substring(9);
                                             document.getElementById("export_"+id_num).style.display = "none";
                                             document.getElementById("delete_"+id_num).style.display = "none";  
                                          }
                                  }
                               Export_All_btn.style.display = "none" ; 
                               Compare_All_btn.style.display = "none" ;
                               Delete_All_btn.style.display = "" ;
                               Show_Valid.style.display = "none" ;
                               Show_inValid.style.display = "none" ;
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
                                                 document.getElementById("export_"+id_num).style.display = "none";
                                                 document.getElementById("delete_"+id_num).style.display = "none"; 
                                              }
                                      }
                                    id_num = thisId.substring(9);
                                    document.getElementById("export_"+id_num).style.display = "";
                                    document.getElementById("delete_"+id_num).style.display = ""; 

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
                                                        document.getElementById("export_"+id_num).style.display = "";
                                                         document.getElementById("delete_"+id_num).style.display = "";  
                                                      }
                                                    else 
                                                      {
                                                         document.getElementById("export_"+id_num).style.display = "none";
                                                         document.getElementById("delete_"+id_num).style.display = "none"; 
                                                      }
                                                  }
                                               else
                                                  {
                                                    document.getElementById("export_"+id_num).style.display = "";
                                                    document.getElementById("delete_"+id_num).style.display = "";  
                                                  }  
                                                 

                                              }
                                      }
                                  }    

                              Export_All_btn.style.display = "none" ;
                              Compare_All_btn.style.display = "none" ;
                              Delete_All_btn.style.display = "none" ;
                              Show_Valid.style.display = "" ;
                              Show_inValid.style.display = "" ;
                             }
                 }
       }
