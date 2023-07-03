document.addEventListener("DOMContentLoaded", function() {
    var form = document.querySelector("form");
    var resultDiv = document.getElementById("result");
  
    form.addEventListener("submit", function(event) {
      event.preventDefault();
  
      // Get form data
      var formData = new FormData(form);
  
      // Create an object to store the form values
      var data = {};
  
      // Iterate over form fields and store values in the data object
      for (var pair of formData.entries()) {
        data[pair[0]] = pair[1];
      }
  
      // Perform credit risk modeling and determine loan approval
      var isGoodAccount = performCreditRiskModeling(data);
  
      // Display loan approval result
      if (isGoodAccount) {
        resultDiv.textContent = "Good account: Loan can be provided";
        resultDiv.style.color = "green";
      } else {
        resultDiv.textContent = "Bad account: Loan cannot be provided";
        resultDiv.style.color = "red";
      }
    });
  
    // Function to perform credit risk modeling
    function performCreditRiskModeling(data) {
      // Perform your credit risk modeling calculations here
      // Based on the provided data, determine if it's a good or bad account for providing a loan
      // You can customize this function according to your specific credit risk modeling algorithm
  
      // Example logic: If the age is greater than 18 and credit_amount is less than 5000, consider it a good account
      if (parseInt(data.age) > 18 && parseInt(data.credit_amount) < 5000) {
        return true;
      } else {
        return false;
      }
    }
  });
  