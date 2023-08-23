const toggleLink = document.getElementById('toggleLink');
const feedbackContainer = document.getElementById('feedbackContainer');
const textarea = document.getElementById('fixedTextarea');
const charCount = document.getElementById('charCount');

textarea.addEventListener('input', function() {
  const maxLength = parseInt(textarea.getAttribute('maxlength'));
  const remainingChars = maxLength - textarea.value.length;
  charCount.textContent = `Caracteres restantes: ${remainingChars}`;
});
toggleLink.addEventListener('click', () => {
  feedbackContainer.classList.toggle('open');
  toggleLink.style.display = 'none';
});
// Função para fechar o painel e mostrar o botão novamente
function fecharPainel() {
  feedbackContainer.classList.remove('open');
  toggleLink.style.display = 'block';  // Mostra o botão novamente
}

// Adicione um evento de clique a um elemento para chamar a função fecharPainel
const fecharButton = document.getElementById('fecharButton');
fecharButton.addEventListener('click', fecharPainel);