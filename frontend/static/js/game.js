const data = document.currentScript.dataset;
const word = data.word;
let lives = parseInt(data.lives);

const wordElement = document.querySelector("#word");
const livesCounterElement = document.querySelector("#lives-counter");
const gameOverElement = document.querySelector("#game-over");

const disableAllButtons = () => {
  const buttons = document.querySelectorAll(".letter-button");
  for (btn of buttons) {
    btn.disabled = true;
  }
};

const playerWon = () => {
  disableAllButtons();
  gameOverElement.classList.toggle("hidden");
  const messageElement = gameOverElement.querySelector("#message");
  messageElement.classList.add("text-green-400");
  messageElement.textContent = `Congratulations you won with ${lives} lives left !!`;
};

const playerLost = () => {
  disableAllButtons();
  gameOverElement.classList.toggle("hidden");
  const messageElement = gameOverElement.querySelector("#message");
  messageElement.classList.add("text-red-400");
  messageElement.textContent = `Game over you lost !! the word was "${word}"`;
  const letterElements = wordElement.querySelectorAll("*");
  for (ele of letterElements) {
    const letter = ele.id.split("-").at(-1);
    ele.textContent = letter;
  }
};

const checkLetter = (event, letter) => {
  const btn = event.target;
  btn.disabled = true;

  // Check if the word contains the letter
  if (word.includes(letter)) {
    btn.className = "bg-green-500 text-white font-bold py-1.5 px-3 rounded";
    const letterElements = wordElement.querySelectorAll(`#letter-${letter}`);
    for (ele of letterElements) {
      ele.textContent = letter;
    }
  } else {
    btn.className = "bg-red-500 text-white font-bold py-1.5 px-3 rounded";
    lives -= 1;
    livesCounterElement.textContent = lives;
  }

  // Check if the game ended
  const currentWord = wordElement.textContent.replace(/\s+/g, "");
  const isWin = currentWord == word && lives > 0;
  if (isWin) {
    playerWon();
  }
  const isGameOver = lives <= 0;
  if (isGameOver) {
    playerLost();
  }
};
