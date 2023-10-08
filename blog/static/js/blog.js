// Get the grid container element
const gridContainer = document.getElementById("grid-container");

// Width calculation function
function setVars() {
	const gridItems = gridContainer.children;
    const divWidth = gridContainer.offsetWidth;
    const calculatedWidth = (divWidth - 120) / 3

    // Set width depending on screen size
    if (window.matchMedia("(min-width: 768px)").matches) {
        for (let item of gridItems) {
            // For desktop screens
            item.style.maxWidth = `${calculatedWidth}px`;
        }
    } else if (window.matchMedia("(max-width: 768px)").matches) {
        for (let item of gridItems) {
            // For mobile screens
		    item.style.maxWidth = "max-content";
        }
    } else {
        for (let item of gridItems) {
            // For mobile screens
		    item.style.maxWidth = "auto";
        }
    }
}

// Set initial
setVars();

// Update dynamically
window.addEventListener("resize", setVars);
