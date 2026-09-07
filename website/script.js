const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) entry.target.classList.add('visible');
  });
}, { threshold: 0.12 });

document.querySelectorAll('.section, .closing-section').forEach((element) => {
  element.classList.add('reveal');
  observer.observe(element);
});
