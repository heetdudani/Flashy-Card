

// Flashcard Flip Functionality
function flipCard() {
  const card = document.getElementById("demo-card");
  card.classList.toggle("is-flipped");
}

// Sample function for next card (would be replaced with real functionality)
function nextCard() {
  const card = document.getElementById("demo-card");
  card.classList.remove("is-flipped");

  // In a real implementation, this would fetch the next card from a deck
  setTimeout(() => {
    alert(
      "In the full application, this would load the next flashcard in your deck."
    );
  }, 150);
}

// Mobile Menu Toggle
document.addEventListener("DOMContentLoaded", function () {
  const mobileMenuButton = document.createElement("div");
  mobileMenuButton.className = "sm:hidden flex items-center";
  mobileMenuButton.innerHTML = `
                <button id="mobile-menu-button" type="button" class="inline-flex items-center justify-center p-2 rounded-md text-gray-500 hover:text-gray-900 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500">
                    <span class="sr-only">Open main menu</span>
                    <svg class="block h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            `;

  document.querySelector("nav .flex").appendChild(mobileMenuButton);

  const mobileMenuButtonEl = document.getElementById("mobile-menu-button");
  const closeMenuButton = document.getElementById("close-menu");
  const mobileMenu = document.getElementById("mobile-menu");

  mobileMenuButtonEl.addEventListener("click", function () {
    mobileMenu.classList.remove("hidden");
  });

  closeMenuButton.addEventListener("click", function () {
    mobileMenu.classList.add("hidden");
  });
});

// profile edit********************

// Modal functions
function showEditModal() {
  document.getElementById("editProfileModal").classList.remove("hidden");
}

function hideEditModal() {
  document.getElementById("editProfileModal").classList.add("hidden");
}

function saveProfileChanges() {
  // Get form values
  const fullName = document.getElementById("fullName").value;
  const occupation = document.getElementById("occupation").value;
  const location = document.getElementById("location").value;
  const mobile = document.getElementById("mobile").value;

  // Update profile display (you would also include AJAX to save to server in real app)
  document.querySelector(".profile-name").textContent = fullName;
  document.querySelector(".profile-occupation").textContent = occupation;
  document.querySelector(".profile-location").textContent = location;
  document.querySelector(".profile-mobile").textContent = mobile;

  hideEditModal();
}

// Pre-fill current values when modal opens
document.getElementById("editProfileModal").addEventListener("click", () => {
  document.getElementById("fullName").value =
    document.querySelector(".profile-name").textContent;
  document.getElementById("occupation").value = document.querySelector(
    ".profile-occupation"
  ).textContent;
  document.getElementById("location").value = document
    .querySelector(".profile-location")
    .textContent.match(/:\s*(.*)/)[1];
  document.getElementById("mobile").value = document
    .querySelector(".profile-mobile")
    .textContent.match(/:\s*(.*)/)[1];
});
