// Get the grid container element and items
const gridContainer = document.getElementById("grid-container");
const gridItems = gridContainer.children;

// Width calculation function
function updateWidth() {
    let divWidth = gridContainer.offsetWidth;
    let calculatedWidth = (divWidth - 120) / 3

    // Set width depending on screen size
    if (window.matchMedia("(max-width: 768px)").matches) {
        for (let item of gridItems) {
            // For mobile screens
            item.style.width = "96%";
        }
    } else if (window.matchMedia("(min-width: 768px)").matches) {
        for (let item of gridItems) {
            // For desktop screens
            item.style.width = `${calculatedWidth}px`;
        }
    }
}

// Height calculation function
function updateHeight() {
	let newHeight = 0;
	for (let item of gridItems) {
		let itemHeight = item.getBoundingClientRect().height;
		if (itemHeight > newHeight) {
		    newHeight = itemHeight;
		}
	}
    for (let item of gridItems) {
        // Set same height for every item
	    item.style.height = `${newHeight}px`;
	}
}

// Combine resizes
function updateVars() {
    updateWidth();
    updateHeight();
}

// Initial sizes
updateVars();

// Update width dynamically
window.addEventListener("resize", updateWidth);
