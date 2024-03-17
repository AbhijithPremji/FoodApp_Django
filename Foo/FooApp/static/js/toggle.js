//  // JavaScript logic for filtering items when a category is clicked
//  document.addEventListener('DOMContentLoaded', function () {
//     // Get all filter menu items
//     var filterMenuItems = document.querySelectorAll('.filters_menu li');

//     // Add click event listener to each filter menu item
//     filterMenuItems.forEach(function (item) {
//         item.addEventListener('click', function () {
//             var selectedCategory = this.textContent.trim(); // Get the text content of the clicked li

//             // Hide all items
//             var allItems = document.querySelectorAll('.filters-content .all');
//             allItems.forEach(function (item) {
//                 item.style.display = 'none';
//             });

//             // Show items with selected category
//             if (selectedCategory === 'All') {
//                 allItems.forEach(function (item) {
//                     item.style.display = 'block';
//                 });
//             } else {
//                 var selectedItems = document.querySelectorAll('.filters-content .' + selectedCategory);
//                 selectedItems.forEach(function (item) {
//                     item.style.display = 'block';
//                 });
//             }
//         });
//     });
// });