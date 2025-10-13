document.addEventListener('DOMContentLoaded', () => {
  const typing = document.getElementById('typing');
  const text = 'Hi, I\'m Leroy Smith';
  let index = 0;
  function type() {
    if (index < text.length) {
      typing.textContent += text.charAt(index);
      index++;
      setTimeout(type, 100);
    }
  }
  type();
});
