document.addEventListener("DOMContentLoaded", function () {
  // Example: Form validation
  const form = document.querySelector("form");
  if (form) {
    form.addEventListener("submit", function (event) {
      const inputs = form.querySelectorAll("input, textarea, select");
      let valid = true;

      inputs.forEach((input) => {
        if (input.hasAttribute("required") && !input.value.trim()) {
          valid = false;
          input.classList.add("error");
          displayError(input, "This field is required.");
        } else {
          input.classList.remove("error");
          clearError(input);
        }
      });

      if (!valid) {
        event.preventDefault();
      }
    });
  }

  // Example: Toggle visibility of elements
  const toggleButtons = document.querySelectorAll(".toggle-button");
  toggleButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const targetId = this.getAttribute("data-target");
      const targetElement = document.getElementById(targetId);
      if (targetElement) {
        targetElement.classList.toggle("hidden");
      }
    });
  });

  // Function to display error messages
  function displayError(element, message) {
    let error = element.nextElementSibling;
    if (error && error.classList.contains("error")) {
      error.textContent = message;
    } else {
      error = document.createElement("div");
      error.classList.add("error");
      error.textContent = message;
      element.parentNode.insertBefore(error, element.nextSibling);
    }
  }

  // Function to clear error messages
  function clearError(element) {
    const error = element.nextElementSibling;
    if (error && error.classList.contains("error")) {
      error.textContent = "";
    }
  }
});
