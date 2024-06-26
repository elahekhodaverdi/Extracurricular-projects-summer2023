document.addEventListener("DOMContentLoaded", function() {
  // Function to calculate and update cost details
  function calculateCosts() {
      let sum = 0;
      document.querySelectorAll(".item").forEach(function(item) {
          const quantity = parseInt(item.querySelector(".quantity-value").textContent);
          const cost = parseFloat(item.querySelector(".item-cost").textContent.replace('$', ''));
          const itemTotalCost = quantity * cost;
          sum += itemTotalCost;
          item.querySelector(".all-i-cost").textContent = `$${itemTotalCost.toFixed(0)}`;
      });

      const discount = sum * 0.05;
      const delivery = sum * 0.03;
      const total = sum - discount + delivery;

      document.getElementById("sum").textContent = `$${sum.toFixed(2)}`;
      document.getElementById("discount").querySelector("td").textContent = `$${discount.toFixed(2)}`;
      document.getElementById("delivery").querySelector("td").textContent = `$${delivery.toFixed(2)}`;
      document.getElementById("total").querySelector("td").textContent = `$${total.toFixed(2)}`;
  }

  // Initial calculation on page load
  calculateCosts();

  // Update quantities and recalculate costs on plus/minus button click
  document.querySelectorAll(".quantity").forEach(function(quantityDiv) {
      let minus = quantityDiv.querySelector(".minus");
      let plus = quantityDiv.querySelector(".plus");
      let quantityValue = quantityDiv.querySelector(".quantity-value");

      minus.addEventListener("click", function() {
          let currentValue = parseInt(quantityValue.textContent);
          if (currentValue > 1) {
              quantityValue.textContent = currentValue - 1;
              calculateCosts();
          }
      });

      plus.addEventListener("click", function() {
          let currentValue = parseInt(quantityValue.textContent);
          quantityValue.textContent = currentValue + 1;
          calculateCosts();
      });
  });
});
