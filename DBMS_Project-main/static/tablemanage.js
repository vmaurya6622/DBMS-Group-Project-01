
console.log("tablemanage aa gya")

function changedataTable(data, tableid) {
    var tableBody = document.querySelector("#" + tableid + " tbody");

    // Clear existing table rows
    tableBody.innerHTML = '';

    // Add new records to the table body
    data.forEach(function(rowData) {
        var newRow = tableBody.insertRow();
        Object.values(rowData).forEach(function(cellData) {
            var newCell = newRow.insertCell();
            newCell.textContent = cellData;
        });
    });
}


async function searchTable(tablenum,searchQuery,frompage) {
    console.log("pass")
    var resp= await $.ajax({
            type: "POST",
            url: "/searchadmin",  // Flask route for handling button click
            contentType: "application/json", // Set content type to JSON
            data: JSON.stringify({sn: searchQuery, tn: tablenum, page: frompage}), // Convert data to JSON string
            success: function(response) {
            // Handle the response from the Flask backend
            console.log(response["res"]);
            console.log(response["tn"]);
        }
    })


    console.log("aa gya kaafi aage");
    console.log(resp);
    return resp;
}
