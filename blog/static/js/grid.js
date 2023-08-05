// Get the grid container element
const gridContainer = document.getElementById("grid-container");

// Calculate fixed-width
function calculateWidth() {
    const divWidth = gridContainer.offsetWidth;
    const calculatedWidth = (divWidth - 120) / 3
    return calculatedWidth
}

function updateRootVar() {
    const resultVar = calculateWidth();
    document.documentElement.style.setProperty("--pg-width", `${resultVar}px`);
}

updateRootVar();
window.addEventListener("resize", updateRootVar);


// Calculate largest hight and assign to containers
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
