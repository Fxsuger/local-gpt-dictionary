chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "lookupWithGPT",
    title: "Look up with GPT Dictionary",
    contexts: ["selection"]
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "lookupWithGPT" && info.selectionText) {
    chrome.storage.local.set({ selectedText: info.selectionText }, () => {
      chrome.sidePanel.open({ windowId: tab.windowId });
    });
  }
});
