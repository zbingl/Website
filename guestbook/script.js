
function saveInput() {
    var fileInput = document.getElementById('fileInput');
    var fileDisplayArea = document.getElementById('guestBook');
    fileDisplayArea.innerText = fileInput.value;
}