
function arrayToTable(tableData) { ////python -m http.server 8888
    var table = $('<table></table>');
    $(tableData).each(function (i, rowData) {
        var row = $('<tr></tr>');
        $(rowData).each(function (j, cellData) {
            row.append($('<td>'+cellData+'</td>'));
        });
        table.append(row);
    });
    return table;
}

$.ajax({
    type: "GET",
    url: "http://127.0.0.1:8888/info.csv",
    success: function (data) {
        $('.JSData').append(arrayToTable(Papa.parse(data).data));
    }
});
