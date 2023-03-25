const wordsList = document.querySelector("#words-list");
const addWordForm = document.querySelector("#word-form");
const restoreDefaultsBtn = document.querySelector("#restore-button");
const deleteAllBtn = document.querySelector("#delete-all-button");

const addWordUrl = addWordForm.dataset.url;
const restoreDefaultsUrl = restoreDefaultsBtn.dataset.url;
const deleteAllUrl = deleteAllBtn.dataset.url;

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
