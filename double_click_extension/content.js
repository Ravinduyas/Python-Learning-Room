document.addEventListener('dblclick', (event) => {
  if (event.target.tagName === 'IMG') {
    const imageUrl = event.target.src;
    const imageName = imageUrl.split('/').pop().split('?')[0];

    chrome.runtime.sendMessage(
      {
        action: "downloadImage",
        url: imageUrl,
        filename: imageName
      },
      (response) => {
        if (response && response.success) {
          console.log('Image download started.');
        } else {
          console.log('Image download failed.');
        }
      }
    );
  }
});
