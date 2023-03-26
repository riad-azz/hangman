const alertContainer = document.querySelector("#alert-container");
const alertMessage = alertContainer.querySelector("#alert-message");
const alertButton = alertContainer.querySelector("#alert-button");

const showAlert = (message) => {
  alertContainer.classList.remove("hidden");
  alertMessage.textContent = message;
};

const closeAlert = () => {
  alertContainer.classList.add("hidden");
};

alertButton.onclick = closeAlert;
