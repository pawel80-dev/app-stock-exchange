var array = [
    ['Car', 'Top Speed', 'Price'],
    ['Chevrolet', '120mph', '$10,000'],
    ['Pontiac', '140pmh', '$20,000']
  ] // Creating a data array which a loop will source from

var table = document.createElement('table');
document.body.appendChild(table); // Drew the main table node on the document

array.forEach(function(row) {
  var tr = table.insertRow(); //Create a new row

  row.forEach(function(column) {
    var td = tr.insertCell();
    td.innerText = column; // Take string from placeholder variable and append it to <tr> node
  });
});