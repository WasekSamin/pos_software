const customerChart = document.querySelector("#customer_chart");
const transactionChart = document.querySelector("#transaction_chat");
let customerData = null,
  transactionData = null;
let getCustomerData = [],
  getTransactionData = [];

if (customerChart) {
  customerData = JSON.parse(customerChart.value);
}

if (transactionChart) {
  transactionData = JSON.parse(transactionChart.value);
}

console.log(customerData);
console.log(transactionData);

if (customerData != null && customerData.length > 0) {
  customerData.map((custData) => {
    let k = Object.keys(custData);
    let v = Object.values(custData);

    if (k[0] === "1") {
      getCustomerData[0] = v[0];
    } else if (k[0] === "2") {
      getCustomerData[1] = v[0];
    } else if (k[0] === "3") {
      getCustomerData[2] = v[0];
    } else if (k[0] === "4") {
      getCustomerData[3] = v[0];
    } else if (k[0] === "5") {
      getCustomerData[4] = v[0];
    } else if (k[0] === "6") {
      getCustomerData[5] = v[0];
    } else if (k[0] === "7") {
      getCustomerData[6] = v[0];
    } else if (k[0] === "8") {
      getCustomerData[7] = v[0];
    } else if (k[0] === "9") {
      getCustomerData[8] = v[0];
    } else if (k[0] === "10") {
      getCustomerData[9] = v[0];
    } else if (k[0] === "11") {
      getCustomerData[10] = v[0];
    } else if (k[0] === "12") {
      getCustomerData[11] = v[0];
    }
  });
}

if (transactionData != null && transactionData.length > 0) {
  transactionData.map((transData) => {
    let k = Object.keys(transData);
    let v = Object.values(transData);

    if (k[0] === "1") {
      getTransactionData[0] = v[0];
    } else if (k[0] === "2") {
      getTransactionData[1] = v[0];
    } else if (k[0] === "3") {
      getTransactionData[2] = v[0];
    } else if (k[0] === "4") {
      getTransactionData[3] = v[0];
    } else if (k[0] === "5") {
      getTransactionData[4] = v[0];
    } else if (k[0] === "6") {
      getTransactionData[5] = v[0];
    } else if (k[0] === "7") {
      getTransactionData[6] = v[0];
    } else if (k[0] === "8") {
      getTransactionData[7] = v[0];
    } else if (k[0] === "9") {
      getTransactionData[8] = v[0];
    } else if (k[0] === "10") {
      getTransactionData[9] = v[0];
    } else if (k[0] === "11") {
      getTransactionData[10] = v[0];
    } else if (k[0] === "12") {
      getTransactionData[11] = v[0];
    }
  });
}

console.log(getTransactionData);

// chart js
const ctx1 = document.getElementById("myChart1").getContext("2d");
const myChart1 = new Chart(ctx1, {
  type: "bar",
  data: {
    labels: [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ],
    datasets: [
      {
        label: "Customer",
        // data: [1, 12, 12, 12,12, 12, 12, 12,12, 12, 12, 12],
        data: getCustomerData,
        backgroundColor: [
          "rgba(255, 99, 132, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(255, 206, 86, 0.2)",
          "rgba(75, 192, 192, 0.2)",
          "rgba(153, 102, 255, 0.2)",
          "rgba(255, 159, 64, 0.2)",
          "rgba(255, 99, 132, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(255, 206, 86, 0.2)",
          "rgba(75, 192, 192, 0.2)",
          "rgba(153, 102, 255, 0.2)",
          "rgba(255, 159, 64, 0.2)",
        ],
        borderColor: [
          "rgba(255, 99, 132, 1)",
          "rgba(54, 162, 235, 1)",
          "rgba(255, 206, 86, 1)",
          "rgba(75, 192, 192, 1)",
          "rgba(153, 102, 255, 1)",
          "rgba(255, 159, 64, 1)",
          "rgba(255, 99, 132, 1)",
          "rgba(54, 162, 235, 1)",
          "rgba(255, 206, 86, 1)",
          "rgba(75, 192, 192, 1)",
          "rgba(153, 102, 255, 1)",
          "rgba(255, 159, 64, 1)",
        ],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});

const ctx3 = document.getElementById("myChart3").getContext("2d");
// const config = {}
const myChart3 = new Chart(ctx3, {
  type: "bar",
  data: {
    labels: [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ],
    datasets: [
      {
        label: "Transaction",
        data: getTransactionData,
        backgroundColor: [
          "rgba(255, 99, 132, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(255, 206, 86, 0.2)",
          "rgba(75, 192, 192, 0.2)",
          "rgba(153, 102, 255, 0.2)",
          "rgba(255, 159, 64, 0.2)",
          "rgba(255, 99, 132, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(255, 206, 86, 0.2)",
          "rgba(75, 192, 192, 0.2)",
          "rgba(153, 102, 255, 0.2)",
          "rgba(255, 159, 64, 0.2)",
        ],
        borderColor: [
          "rgba(255, 99, 132, 1)",
          "rgba(54, 162, 235, 1)",
          "rgba(255, 206, 86, 1)",
          "rgba(75, 192, 192, 1)",
          "rgba(153, 102, 255, 1)",
          "rgba(255, 159, 64, 1)",
          "rgba(255, 99, 132, 1)",
          "rgba(54, 162, 235, 1)",
          "rgba(255, 206, 86, 1)",
          "rgba(75, 192, 192, 1)",
          "rgba(153, 102, 255, 1)",
          "rgba(255, 159, 64, 1)",
        ],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});
