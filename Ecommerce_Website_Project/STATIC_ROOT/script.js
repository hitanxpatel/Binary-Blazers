document.addEventListener("DOMContentLoaded", function () {
    const logo = document.querySelector(".logo");
    const names = [
        { text: "PACKS", color: "white" },
        { text: "PACKING", color: "orange" },
        { text: "AND", color: "orange" },
        { text: "CONTROL", color: "white" },
        { text: "KIT", color: "lime" },
        { text: "SYSTEM", color: "lime" }
    ];
    let index = 0;

    function changeLogoText() {
        logo.textContent = names[index].text;
        logo.style.color = names[index].color;
        index = (index + 1) % names.length;
    }

    setInterval(changeLogoText, 2000); // Change every 2 seconds
});
