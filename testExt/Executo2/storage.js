var stored = {
    text: "asdf"
  }

function onError(e) {
console.error(e);
}
function checkStoredSettings(storedSettings) {
if (!storedSettings.stored) {
    browser.storage.local.set({stored});
}
}

const gettingStoredSettings = browser.storage.local.get();
gettingStoredSettings.then(checkStoredSettings, onError);
  