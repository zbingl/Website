function _saveInput() {
  const fileInput = document.querySelector<HTMLInputElement>("#fileInput");
  const fileDisplayArea = document.querySelector<HTMLElement>("#guestBook");

  if (!fileInput || !fileDisplayArea) return;

  fileDisplayArea.innerText = fileInput.value;
}
