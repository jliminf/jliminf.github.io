const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#site-nav');
function closeMenu() {
  menuButton?.setAttribute('aria-expanded', 'false');
  navigation?.classList.remove('is-open');
}
menuButton?.addEventListener('click', () => {
  const expanded = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(expanded));
  navigation.classList.toggle('is-open', expanded);
});
navigation?.addEventListener('click', event => {
  if (event.target.closest('a')) closeMenu();
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menuButton?.getAttribute('aria-expanded') === 'true') {
    closeMenu();
    menuButton.focus();
  }
});

const publicationFilters = document.querySelectorAll('[data-filter]');
publicationFilters.forEach(button => button.addEventListener('click', () => {
  const selected = button.dataset.filter;
  publicationFilters.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  let count = 0;
  document.querySelectorAll('[data-publication]').forEach(row => {
    row.hidden = selected !== 'all' && row.dataset.publication !== selected;
    if (!row.hidden) count += 1;
  });
  const status = document.querySelector('#filter-status');
  if (status) status.textContent = `${count} publications shown`;
}));
