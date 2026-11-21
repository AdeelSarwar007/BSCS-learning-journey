const projects = [
    { title: "Grade Checker", desc: "Python program that calculates student grades." },
    { title: "Patient Form", desc: "HTML form with input validation." },
    { title: "AI Patient Triage (FYP)", desc: "ML-based triage and specialist recommendation system." }
];

const projectList = document.getElementById("projectList");

projects.forEach(function (p) {
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = "<h3>" + p.title + "</h3><p>" + p.desc + "</p>";
    projectList.appendChild(card);
});

const themeBtn = document.getElementById("themeBtn");

themeBtn.addEventListener("click", function () {
    document.body.classList.toggle("dark");
});

const form = document.getElementById("contactForm");
const formMsg = document.getElementById("formMsg");

form.addEventListener("submit", function (event) {
    event.preventDefault();

    const name = document.getElementById("nameInput").value;
    const email = document.getElementById("emailInput").value;

    if (name === "" || email === "") {
        formMsg.textContent = "Please fill your name and email.";
        return;
    }

    formMsg.textContent = "Thanks, " + name + "! Your message was received.";
    form.reset();
});