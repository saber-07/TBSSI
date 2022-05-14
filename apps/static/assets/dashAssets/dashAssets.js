  var config = {
    type: 'pie',
    data: {
      datasets: [{
        data: {{ data|safe }},
        backgroundColor: [
          'red', 'blue', '#black', 'pink', 'gray'
        ],
        label: 'Valeur'
      }],
      labels: {{ labels|safe }}
    },
    options: {
      responsive: true
    }
  };

  window.onload = function() {
    var ctx = document.getElementById('pie-chart').getContext('2d');
    window.myPie = new Chart(ctx, config);
  };


