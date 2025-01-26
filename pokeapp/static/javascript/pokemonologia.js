const moreOptionsIcon = document.querySelector('.moreOptions');
const sidebar = document.querySelector('.more-options');
const blurOverlay = document.querySelector('.blur');
const Cards = document.querySelectorAll(".card")
const ButtonsClasses = document.querySelectorAll(".more-options img")
const IconPokemon = document.querySelector(".icon-pokemon")

Cards.forEach(card => {
    classe = card.querySelector("#classe").value
    console.log(classe)
    if (classe !== "Normal"){
        card.style.display = "none"
    }
});

ButtonsClasses.forEach(button =>{
    button.addEventListener("click", ()=>{
        IconPokemon.src = `/static/icons/${button.id.toLowerCase()}.svg`;
        classe_button = button.id
        Cards.forEach(card => {
            classe = card.querySelector("#classe").value
            if (classe !== classe_button){
                card.style.display = "none"
            }else{
                card.style.display = "flex"
            }
        });
    })
})

function toggleSidebar() {
    const isActive = sidebar.classList.contains('active');
    if (isActive) {
        sidebar.classList.remove('active');
        blurOverlay.classList.remove('active');
        setTimeout(() => sidebar.style.display = "none", 300);
    } else {
        sidebar.style.display = "flex";
        setTimeout(() => {
            sidebar.classList.add('active');
            blurOverlay.classList.add('active');
        }, 10);
    }
}

moreOptionsIcon.addEventListener('click', toggleSidebar);
blurOverlay.addEventListener('click', toggleSidebar);
