// *****************flash card*********************
const flashcard = document.getElementById("flashcard");
const flashcardQuestion = document.getElementById("flashcard-question");
const flashcardAnswer = document.getElementById("flashcard-answer");
const prevCardBtn = document.getElementById("prev-card");
const revealAnswerBtn = document.getElementById("reveal-answer");
const nextCardBtn = document.getElementById("next-card");
const currentCardIndexSpan = document.getElementById("current-card-index");
const totalCardsSpan = document.getElementById("total-cards");
const progressBar = document.getElementById("progressBar");
const completionMessage = document.getElementById("completionMessage");

console.log('{{cdata}}')

const cards = [
  {
    question: "What is JavaScript primarily used for?",
    answer:
      "Web development (frontend and backend), mobile apps, desktop apps, etc.",
  },
  {
    question: "What is a variable in programming?",
    answer: "A named storage location for data.",
  },
  { question: "What does DOM stand for?", answer: "Document Object Model" },
  {
    question: "Which keyword is used to declare a constant in JavaScript?",
    answer: "`const`",
  },
  {
    question: "What is an array?",
    answer:
      "A data structure that stores a collection of elements, typically of the same type, in a contiguous memory location.",
  },
];

let currentCardIndex = 0;

function updateCard() {
  flashcard.classList.remove("flipped"); // Ensure card is not flipped when changing content
  flashcardQuestion.textContent = cards[currentCardIndex].question;
  flashcardQuestion.textContent = cards[currentCardIndex].question;
  flashcardAnswer.textContent = cards[currentCardIndex].answer;
  currentCardIndexSpan.textContent = currentCardIndex + 1;
  totalCardsSpan.textContent = cards.length;
  updateProgressBar();
  hideCompletionMessage(); // Hide message when navigating
}

function updateProgressBar() {
  const progress = ((currentCardIndex + 1) / cards.length) * 100;
  progressBar.style.width = `${progress}%`;
}

function showCompletionMessage() {
  completionMessage.classList.add("show");
}

function hideCompletionMessage() {
  completionMessage.classList.remove("show");
}

// Event Listeners
// Removed the direct click listener on flashcard to give full control to the button
// flashcard.addEventListener('click', () => {
//   flashcard.classList.toggle('flipped');
// });

revealAnswerBtn.addEventListener("click", (e) => {
  e.stopPropagation(); // Prevent any parent click handlers
  flashcard.classList.toggle("flipped"); // Toggle the flipped class
});

prevCardBtn.addEventListener("click", (e) => {
  e.stopPropagation();
  if (currentCardIndex > 0) {
    currentCardIndex--;
    updateCard();
  }
});

nextCardBtn.addEventListener("click", (e) => {
  e.stopPropagation();
  if (currentCardIndex < cards.length - 1) {
    currentCardIndex++;
    updateCard();
  } else {
    // Reached the end of the deck
    showCompletionMessage();
  }
});

// Initial load
updateCard();
