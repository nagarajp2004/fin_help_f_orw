// ✅ Open Modal
function openModal() {
  document.getElementById('askDoubtModal').style.display = 'flex';
}

// ✅ Close Modal
function closeModal() {
  document.getElementById('askDoubtModal').style.display = 'none';
}

// ✅ Submit Doubt
function submitDoubt() {
  let doubtText = document.getElementById('doubtText').value.trim();
  if (doubtText === "") {
      alert("Please enter a doubt before submitting.");
  } else {
      alert("Doubt submitted successfully!");
      closeModal();
  }
}

// ✅ Close Modal When Clicking Outside
window.onclick = function(event) {
  let modal = document.getElementById('askDoubtModal');
  if (event.target === modal) {
      closeModal();
  }
};

// ✅ Mobile Menu Toggle
document.getElementById("menu-btn").addEventListener("click", function () {
  let menu = document.getElementById("menu");
  menu.classList.toggle("active");
});

