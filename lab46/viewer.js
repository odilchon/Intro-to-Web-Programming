const popup = document.getElementById("popup");
const popupImage = document.getElementById("popupImage");
const exitBtn = document.getElementById("exitBtn");
const nextBtn = document.getElementById("next");
const prevBtn = document.getElementById("previous");
const photoWrapper = document.getElementById("photoWrapper");

const photos = [
    "assets/mountain.jpg",
    "assets/forest.jpg",
    "assets/beach.jpg",
    "assets/city.jpg",
    "assets/desert.jpg",
    "assets/lake.jpg"
];

let activeIndex = 0;

function buildGallery() {
    photos.forEach((path, i) => {
        const img = document.createElement("img");
        img.src = path;
        img.alt = `Nature ${i+1}`;
        photoWrapper.appendChild(img);

        img.addEventListener("click", () => {
            openPopup(i);
        });
    });
}

function openPopup(index) {
    activeIndex = index;
    popupImage.src = photos[activeIndex];
    popup.classList.add("active");
    localStorage.setItem("lastPhoto", photos[activeIndex]);
}

function closePopup() {
    popup.classList.remove("active");
}

function showNext() {
    activeIndex = (activeIndex + 1) % photos.length;
    switchImage();
}

function showPrev() {
    activeIndex = (activeIndex - 1 + photos.length) % photos.length;
    switchImage();
}

function switchImage() {
    popupImage.src = photos[activeIndex];
    popupImage.classList.add("zoom-effect");
    setTimeout(() => popupImage.classList.remove("zoom-effect"), 250);
    localStorage.setItem("lastPhoto", photos[activeIndex]);
}

exitBtn.addEventListener("click", closePopup);
nextBtn.addEventListener("click", showNext);
prevBtn.addEventListener("click", showPrev);


window.addEventListener("click", (e) => {
    if (e.target === popup) closePopup();
});

window.addEventListener("load", () => {
    buildGallery();
    const saved = localStorage.getItem("lastPhoto");
    if (saved && photos.includes(saved)) {
        activeIndex = photos.indexOf(saved);
        popupImage.src = saved;
        popup.classList.add("active");
    }
});