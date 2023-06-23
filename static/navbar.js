let nav_items = document.querySelectorAll('.nav-item');
let icons = document.querySelectorAll('.icon');

nav_items.forEach((item, index) => {
  item.addEventListener('mouseover', () => {
    icons[index].style.color = 'blue';
  });

  item.addEventListener('mouseout', () => {
    icons[index].style.color = 'black';
  });
});
