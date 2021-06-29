const tabs = document.querySelectorAll("[data-tab-target]");
const tabcon = document.querySelectorAll("[data-tab-content]");
tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
        tabs.forEach((tab_others) => {
            tab_others.classList.remove("active-tab");
        })
        tab.classList.add("active-tab");
        const target = document.querySelector(tab.dataset.tabTarget);
        tabcon.forEach((tabc_all) => {
            tabc_all.classList.remove("active");
        });
        target.classList.add("active");
    })
})