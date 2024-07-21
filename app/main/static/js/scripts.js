document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.querySelector('input[type="file"]');
    const allowedExtensions = ['pdf', 'doc', 'docx', 'png', 'jpg', 'jpeg'];

    fileInput.addEventListener('change', function() {
        const fileName = fileInput.value.split('\\').pop();
        const fileExtension = fileName.split('.').pop().toLowerCase();

        if (!allowedExtensions.includes(fileExtension)) {
            alert('Invalid file type. Please upload a PDF, Word document, or image file.');
            fileInput.value = ''; // Clear the input
        }
    });
});
