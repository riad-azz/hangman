const livesInput = document.querySelector("#lives");
const updateLivesForm = document.querySelector("#lives-form");
const livesMessage = document.querySelector("#lives-message");
const wordsList = document.querySelector("#words-list");
const addWordForm = document.querySelector("#word-form");
const wordsMessage = document.querySelector("#word-message");
const restoreDefaultsBtn = document.querySelector("#restore-button");
const deleteAllBtn = document.querySelector("#delete-all-button");

const updateLivesUrl = updateLivesForm.dataset.url;
const addWordUrl = addWordForm.dataset.url;
const restoreDefaultsUrl = restoreDefaultsBtn.dataset.url;
const deleteAllUrl = deleteAllBtn.dataset.url;

updateLivesForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const formData = new FormData(updateLivesForm);
  fetch(updateLivesUrl, {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      livesInput.value = data.lives;
      showAlert(data.message, data.category);
    })
    .catch((error) => console.error(error));
});

addWordForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const formData = new FormData(addWordForm);
  fetch(addWordUrl, {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      wordsList.innerHTML = data.template;
      addWordForm.reset();
    })
    .catch((error) => console.error(error));
});

const restoreDefaults = () => {
  fetch(restoreDefaultsUrl)
    .then((response) => response.json())
    .then((data) => {
      wordsList.innerHTML = data.template;
    })
    .catch((error) => console.error(error));
};

const deleteAll = () => {
  fetch(deleteAllUrl)
    .then((response) => response.json())
    .then((data) => {
      wordsList.innerHTML = data.template;
    })
    .catch((error) => console.error(error));
};

restoreDefaultsBtn.onclick = restoreDefaults;
deleteAllBtn.onclick = deleteAll;
