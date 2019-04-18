function arrayToTable(tableData) { ////python -m http.server 8888
       var table = $('<div class="JSData"></div>');
       $(tableData).each(function (i, rowData) {
           var row = $('<div></div>');
           $(rowData).each(function (j, cellData) {
               row.append($('<p>'+cellData+'</p>'));
           });
           table.append(row);
       });
       return table;
   }

   $.ajax({
       type: "GET",
       url: "http://192.168.1.23:3000/data.txt",
       success: function (data) {
           $('body').append(arrayToTable(Papa.parse(data).data));
       }
   });
