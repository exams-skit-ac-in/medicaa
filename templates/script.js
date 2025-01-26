// Toggle the dropdown menus for Doctors, Medicals, and Hospitals
function toggleMenu(menu) {
    const submenu = document.getElementById(`submenu-${menu}`);
    submenu.style.display = submenu.style.display === "block" ? "none" : "block";
}

// Toggle the Profile menu (Log out, My Profile)
function toggleProfileMenu() {
    const submenu = document.getElementById("submenu-profile");
    submenu.style.display = submenu.style.display === "block" ? "none" : "block";
}

// Toggle Chatbot visibility
function toggleChatbot() {
    alert("Chatbot feature is not implemented in this code. You can integrate a chatbot here.");
}
