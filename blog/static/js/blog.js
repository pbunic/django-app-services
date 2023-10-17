// Get the grid container element and items
const gridContainer = document.getElementById("grid-container");
const gridItems = gridContainer.children;

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

// Initialize height sizes
updateHeight();
