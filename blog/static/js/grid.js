// Get the grid container element
const gridContainer = document.getElementById("grid-container");

// first width and height
function updateVars() {
	const gridItems = gridContainer.children;
    const divWidth = gridContainer.offsetWidth;
    const calculatedWidth = (divWidth - 120) / 3

	// Find height of the largest
	let maxHeight = 0;
	for (let item of gridItems) {
		const itemHeight = item.getBoundingClientRect().height;
		if (itemHeight > maxHeight) {
		    maxHeight = itemHeight;
		}
	}

	// Set width and height of the grids
	for (let item of gridItems) {
		item.style.minWidth = `${calculatedWidth}px`;
		item.style.minHeight = `${maxHeight}px`;
	}
}

// new-width
function updateWidth() {
	const gridItems = gridContainer.children;
    const divWidth = gridContainer.offsetWidth;
    const calculatedWidth = (divWidth - 120) / 3

	// Set new width
	for (let item of gridItems) {
		item.style.minWidth = `${calculatedWidth}px`;
	}
}

updateVars();
window.addEventListener("resize", updateWidth);
