const textInput = document.querySelector("#text");

function storeSettings() {
  browser.storage.local.set({
    stored: {
      text: textInput.value,
    }
  });
}

function updateUI(restoredSettings) {
    textInput.value = restoredSettings.stored.text || "";
}

function onError(e) {
  console.error(e);
}

const gettingStoredSettings = browser.storage.local.get();
gettingStoredSettings.then(updateUI, onError);

textInput.addEventListener("blur", storeSettings);
