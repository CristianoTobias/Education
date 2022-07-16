let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
function generateTarget() {
  return Math.floor(Math.random() * 10);
}
function compareGuesses(human, computer, secret) {
  if ((human >= 0) && (human <= 9)){
  return Math.abs(human - secret) <= Math.abs(computer - secret) ? true : false;
}else{
  console.log(alert("Number out of range!"))
}
}
function updateScore(winner) {
  if (winner == "human") {
    humanScore++;
  } else if (winner == "computer") {
    computerScore++;
  }
}
function advanceRound() {
  currentRoundNumber++;
}

