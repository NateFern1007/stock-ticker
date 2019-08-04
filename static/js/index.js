var $TABLE = $('#table');
var $BTN = $('#export-btn');
var $EXPORT = $('#export');

$( document ).ready(function() {
  var schedule = JSON.parse(document.cookie.replace(/\\054/g, ",").replace(/'/g, "\"").match(new RegExp('schedule' + '="([^;]+)"'))[1]["Global Quote"]);
  for (block in schedule) {
    var $clone = $TABLE.find('tr.hide').clone(true).removeClass('hide table-line');
    $clone[0].children[0].textContent = schedule[block]["block"];
    $clone[0].children[1].textContent = schedule[block]["02. name"];
    $clone[0].children[2].textContent = schedule[block]["latest-date"];
    $clone[0].children[3].textContent = schedule[block]["exchange"];
    $clone[0].children[4].textContent = schedule[block]["open"];
    $clone[0].children[5].textContent = schedule[block]["close"];
    $clone[0].children[6].textContent = schedule[block]["high"];
    $clone[0].children[7].textContent = schedule[block]["low"];
    $clone[0].children[8].textContent = schedule[block]["latest-price"];
    $clone[0].children[9].textContent = schedule[block]["delayed-price"];
    $clone[0].children[10].textContent = schedule[block]["previous-close"];
    $clone[0].children[11].textContent = schedule[block]["change"];
    $clone[0].children[12].textContent = schedule[block]["change-percent"];
    $clone[0].children[13].textContent = schedule[block]["Close on Jan 1"];
    $clone[0].children[14].textContent = schedule[block]["Cummulitive Gain/Loss"];
    $clone[0].children[15].textContent = schedule[block]["Cummulative Gain/Loss %"];
    $clone[0].children[16].textContent = schedule[block]["Cummulative Gain/Loss % from Jan 1"];
    $TABLE.find('table').append($clone);
  }
});

$('.table-add').click(function () {
  var $clone = $TABLE.find('tr.hide').clone(true).removeClass('hide table-line');
  $TABLE.find('table').append($clone);
});

$('.table-remove').click(function () {
  $(this).parents('tr').detach();
});

$('.table-up').click(function () {
  var $row = $(this).parents('tr');
  if ($row.index() === 1) return; // Don't go above the header
  $row.prev().before($row.get(0));
});

$('.table-down').click(function () {
  var $row = $(this).parents('tr');
  $row.next().after($row.get(0));
});

// A few jQuery helpers for exporting only
jQuery.fn.pop = [].pop;
jQuery.fn.shift = [].shift;

$BTN.click(function () {
  var $rows = $TABLE.find('tr:not(:hidden)');
  var headers = [];
  var data = [];
  
  // Get the headers (add special header logic here)
  $($rows.shift()).find('th:not(:empty)').each(function () {
    headers.push($(this).text().toLowerCase());
  });
  
  // Turn all existing rows into a loopable array
  $rows.each(function () {
    var $td = $(this).find('td');
    var h = {};
    
    // Use the headers from earlier to name our hash keys
    headers.forEach(function (header, i) {
      h[header] = $td.eq(i).text();   
    });
    
    data.push(h);
  });
  
  // Output the result
  document.cookie = "schedule=" + JSON.stringify(data); // Export JSON data to cookie
  window.location = "save"; // Call python 'save' function
});

