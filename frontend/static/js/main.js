const alertContainer = document.querySelector("#alert-container");
const alertMessage = alertContainer.querySelector("#alert-message");
const alertButton = alertContainer.querySelector("#alert-button");

const showAlert = (message, category) => {
  alertContainer.classList.toggle("hidden");
  alertMessage.textContent = message;
};

const closeAlert = () => {
  alertContainer.classList.toggle("hidden");
};

alertButton.onclick = closeAlert;
