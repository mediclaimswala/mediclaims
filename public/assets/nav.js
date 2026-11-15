// The Services menu is a native <details>, so it works without this file; this only closes it on an outside click or Escape.
(function () {
  function close(except) {
    document.querySelectorAll('details.menu[open]').forEach(function (d) { if (d !== except) d.removeAttribute('open'); });
  }
  document.addEventListener('click', function (e) { close(e.target.closest && e.target.closest('details.menu')); });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    var open = document.querySelector('details.menu[open]');
    if (open) { open.removeAttribute('open'); open.querySelector('summary').focus(); }
  });
})();
