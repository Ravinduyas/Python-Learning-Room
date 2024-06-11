chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "downloadImage") {
    chrome.downloads.download({
      url: request.url,
      filename: request.filename
    }, (downloadId) => {
      sendResponse({success: !!downloadId});
    });
    return true; // Keep the message channel open for sendResponse.
  }
});
