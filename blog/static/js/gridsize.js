// Get the grid container element
const gridContainer = document.getElementById("grid-container");

// Get all grid items within the container
const gridItems = gridContainer.children;

// Find height of the largest
let maxHeight = 0;
for (let item of gridItems) {
    const itemHeight = item.getBoundingClientRect().height;
    if (itemHeight > maxHeight) {
        maxHeight = itemHeight;
    }
}

// Set the min-height of the grids
for (let item of gridItems) {
    item.style.minHeight = `${maxHeight}px`;
}
